from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML

from apscheduler.schedulers.background import BackgroundScheduler
import fcntl

from api import app, db
from api import models

from api.update_rates import update_rates

from flask import request, jsonify
from api.queries import resolve_exchangerates, resolve_exchangerate, create_exchangerate

query = ObjectType("Query")
mutation = ObjectType("Mutation")
query.set_field("exchangerates", resolver=resolve_exchangerates)
query.set_field("exchangerate", resolver=resolve_exchangerate)
mutation.set_field("create_exchangerate", resolver=create_exchangerate)

type_defs = load_schema_from_path("schemas/schema.graphql")

schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


@app.before_first_request
def initialize_scheduler():
    """Initialize database and fill database with currency data.
        Job runs every 1 hour and inserts new data. 
    """
    # TODO: Change functionality to upsert data, instead having duplicates or inserting same data

    db.create_all()
    print("Set up db")

    try:
        _ = open("scheduler.lock", "w")
        fcntl.lockf(_.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

        scheduler = BackgroundScheduler()
        scheduler.start()

        scheduler.add_job(update_rates, "interval", hours=1)


        scheduler.add_job(update_rates, kwargs={"historic": False})
    except BlockingIOError:
        pass
