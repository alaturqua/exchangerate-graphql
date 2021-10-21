from flask import Flask
from flask.templating import render_template

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from .constants import POSTGRES_URL, FLASK_SECRET_KEY

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = FLASK_SECRET_KEY


db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

#TODO: Iplement unit tests & integration tests & end-2-end tests

@app.route('/')
def index():
    return render_template("index.html")
