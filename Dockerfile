FROM python:3.12.7-alpine3.20

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pipenv install --deploy --ignore-pipfile
