FROM python:3.8.9-slim-buster

LABEL author="Isa Inalcik"


ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT=1 


EXPOSE 5000

RUN mkdir -p code

WORKDIR /code

RUN pip install pipenv

COPY . .

RUN pipenv install --system --deploy --ignore-pipfile

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

ENTRYPOINT flask run --host 0.0.0.0 --port 5000

