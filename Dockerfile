FROM python:3.9-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install "poetry==1.2.2"
COPY poetry.lock pyproject.toml /usr/src/app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

ADD src /usr/src/app/src

EXPOSE 8080

CMD gunicorn  --chdir src "fdk_harvester_bff:create_app()"  --config=src/fdk_harvester_bff/gunicorn_config.py
