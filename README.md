# fdk-harvester-bff
A small service which offers json representations of datasets, dataservices, concepts and informationmodels

## Develop and run locally
### Requirements
- [pyenv](https://github.com/pyenv/pyenv) (recommended)

### Install software:
```
% git clone https://github.com/Informasjonsforvaltning/fdk-harvester-bff.git
% cd fdk-harvester-bff
% pyenv install 3.8
% pyenv local 3.8
% pip install poetry==1.1.3
% pip install nox==2020.8.22
% pip install nox-poetry==0.5.0
% poetry install
```
### Environment variables
To run the service you need to supply a set of environment variables. A simple way to solve this is to supply a .env file in the root directory:
```
HOST = "http://localhost"
HOST_PORT = "8080"
ORGANIZATION_CATALOGUE_BASE_URI=http://localhost:8081
DATASET_HARVESTER_BASE_URL=http://localhost:8081
REFERENCE_DATA_BASE_URI =http://localhost:8081

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
### With docker-compose:
```
% docker-compose up --build
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
