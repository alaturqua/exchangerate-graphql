from .constants import BASE_CURRENCY, HISTORIC_RATES_URL, LAST_90_DAYS_RATES_URL
from .models import ExchangeRate
from datetime import datetime
from defusedxml import ElementTree
import requests
from decimal import Decimal
from main import db
from api import app


def update_rates(historic=False):
    """ Fills database with currency data.
    """
    # TODO: Change functionality to upsert data, instead having duplicates or inserting same data
    # TODO: Implement proper Error Handling

    try:
        r = requests.get(
            HISTORIC_RATES_URL if historic else LAST_90_DAYS_RATES_URL)
        envelope = ElementTree.fromstring(r.content)

        namespaces = {
            "gesmes": "http://www.gesmes.org/xml/2002-08-01",
            "eurofxref": "http://www.ecb.int/vocabulary/2002-08-01/eurofxref",
        }

        data = envelope.findall(
            "./eurofxref:Cube/eurofxref:Cube[@time]", namespaces)
        for d in data:
            time = datetime.strptime(d.attrib["time"], "%Y-%m-%d").date()
            rates = d.getchildren()
            for c in list(rates):
                base = BASE_CURRENCY
                rate = Decimal(c.get("rate"))
                currency_code = c.get('currency')
                date = time
                exchange_rate = ExchangeRate(
                    base=base, rate=rate, currency_code=currency_code, date=date)
                app.logger.debug(
                    f"Creating exchangerate: {exchange_rate.to_dict()}")
                db.session.add(exchange_rate)
                db.session.commit()

    except Exception as e:
        app.logger.error(e)
