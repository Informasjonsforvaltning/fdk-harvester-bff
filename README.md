# fdk-harvester-bff
A small service which offers json representations of datasets, dataservices, concepts and informationmodels

## Develop and run locally
### Requirements
- [pyenv](https://github.com/pyenv/pyenv) (recommended)

### Install software:
```
% git clone https://github.com/Informasjonsforvaltning/fdk-harvester-bff.git
% cd fdk-harvester-bff
% pyenv install 3.8.3
% pyenv install 3.7.7
% pyenv local 3.8.3 3.7.7
% pip install poetry
% pip install nox
% poetry install
```
### Environment variables
To run the service you need to supply a set of environment variables. A simple way to solve this is to supply a .env file in the root directory:
```
HOST = "http://localhost"
HOST_PORT = "8080"
```
### Running the API locally
 Start the endpoint:
```
% poetry shell
% FLASK_APP=fdk_harvester_bff FLASK_ENV=development flask run --port=8080
```
## Running the API in a wsgi-server (gunicorn)
```
% poetry shell
% gunicorn  --chdir src "fdk_harvester_bff:create_app()"  --config=src/fdk_harvester_bff/gunicorn_config.py
```
## Running the wsgi-server in Docker
To build and run the api in a Docker container:
```
% docker build -t digdir/fdk-harvester-bff:latest .
% docker run --env-file .env -p 8080:8080 -d digdir/fdk-harvester-bff:latest
```
## Load data
 - [ ] TODO: document how to load data by using scripts in etl folder of ./scripts
## Running tests
We use [pytest](https://docs.pytest.org/en/latest/) for contract testing.

To run linters, checkers and tests:
```
% nox
```
## Test the endpoint
Regardless if you run the app via Docker or not, in another terminal:
```
% curl --header "Content-Type: application/json" \
  --request POST \
  --data @tests/catalog_1.json \
  http://localhost:8080/catalogs
```
