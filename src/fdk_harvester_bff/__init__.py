"""Package for A small service which offers json representations of datasets in a Flask API."""
import json
import os
from os import environ as env
from typing import Any

from dotenv import load_dotenv
from flask import (
    abort,
    Flask,
    jsonify,
    make_response,
    render_template,
    request,
    Response,
)
import requests
from werkzeug.exceptions import HTTPException, InternalServerError


load_dotenv()
# Hent environ-variables

__version__ = "0.1.0"


def create_app(test_config: Any = None) -> Flask:
    """Create app."""
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ------
    # Routes
    @app.route("/ready", methods=["GET"])
    def isReady() -> str:
        """Ready route function."""
        resp = requests.get(
            f"""{env.get("DATASET_HARVESTER_BASE_URL", "https://datasets.staging.fellesdatakatalog.digdir.no")}/ready"""
        )
        if resp.status_code == 200:
            return "OK"
        else:
            abort(400)

    @app.route("/ping", methods=["GET"])
    def isAlive() -> str:
        """Ping route function."""
        return "OK"

#    @app.route("/datasets/<string:id>", methods=["GET"])
#    def getDatasetById(id: str) -> Response:
#        """Get catalog by id."""
#        dataset = get_dataset_by_id(id)
        # Do the parsing magic here
#        response = make_response()
#        return Response( ## serialize to json )
