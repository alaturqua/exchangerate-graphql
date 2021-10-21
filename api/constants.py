from dotenv import load_dotenv
import os
from os.path import dirname, abspath, join

# Get secrets from .env
path = dirname(dirname(abspath(__file__)))
dotenv_path = join(path, '.env')
load_dotenv(dotenv_path)

# Database credentials
POSTGRES_USERNAME = os.environ.get('POSTGRESQL_USERNAME')
POSTGRES_PASSWORD = os.environ.get('POSTGRESQL_PASSWORD')

# Flask app secret key
FLASK_SECRET_KEY = os.environ.get('TESTSECRETKEY')

# ECB api urls
HISTORIC_RATES_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.xml"
LAST_90_DAYS_RATES_URL = (
    "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml"
)

# Base currency - based on the given currency according exchange rates will be pulled
BASE_CURRENCY = 'EUR'

# Postgres Connection String
POSTGRES_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@db:5432/postgres"
