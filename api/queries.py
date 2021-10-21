from .models import ExchangeRate
from ariadne import convert_kwargs_to_snake_case
from api import db, app


def resolve_exchangerates(obj, info):
    try:
        exchangerates = [exchangerate.to_dict()
                         for exchangerate in ExchangeRate.query.all()]

        payload = {
            "success": True,
            "exchangerates": exchangerates
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

        app.logger.error(payload)

    return payload


@convert_kwargs_to_snake_case
def resolve_exchangerate(obj, info, id):
    try:
        exchangerate = ExchangeRate.query.get(id)
        payload = {
            "success": True,
            "exchangerate": exchangerate.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"ExchangeRate item matching {id} not found"]
        }

        app.logger.error(payload)

    return payload


@convert_kwargs_to_snake_case
def create_exchangerate(obj, info, base, rate, currency_code, date):
    # FIXME: Fix manual data insertion
    try:
        exchangerate = ExchangeRate(
            base=base, rate=rate, currency_code=currency_code, date=date)
        db.session.add(exchangerate)
        db.session.commit()
        payload = {
            "success": True,
            "exchangerate": exchangerate.to_dict()
        }

    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in the format yyyy-mm-dd"]
        }

        app.logger.error(payload)

    return payload
