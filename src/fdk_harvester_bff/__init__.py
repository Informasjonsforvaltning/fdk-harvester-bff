"""Package for A small service which offers json representations of datasets in a Flask API."""
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
from flask_cors import CORS
import simplejson as json

from fdk_harvester_bff.service.services import (
    FetchFromServiceException,
    get_dataset_by_id,
    get_information_model_by_id,
)

load_dotenv()


def create_app(test_config: Any = None) -> Flask:
    """Create app."""
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)

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
        return "OK"

    @app.route("/ping", methods=["GET"])
    def isAlive() -> str:
        """Ping route function."""
        return "OK"

    @app.route("/information-models/<string:id>", methods=["GET"])
    def information_model_by_id(id: str) -> Response:
        """Get catalog by id."""
        try:
            body = json.dumps(get_information_model_by_id(id), iterable_as_array=True)
            return Response(body, status=200, content_type="application/json")
        except FetchFromServiceException as err:
            return Response(status=err.status)

    @app.route("/datasets/<string:id>", methods=["GET"])
    def dataset_by_id(id: str) -> Response:
        """Get catalog by id."""
        try:
            body = json.dumps(get_dataset_by_id(id), iterable_as_array=True)
            return Response(body, status=200, content_type="application/json")
        except FetchFromServiceException as err:
            return Response(err.reason, status=err.status)

    return app
