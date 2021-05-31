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
from flask_restful import Api

import fdk_harvester_bff.routes as routes

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

    # add routes
    api = Api(app)
    api.add_resource(routes.Ping, "/ping")
    api.add_resource(routes.Ready, "/ready")
    api.add_resource(routes.InfoModels, "/information-models/<string:id>")
    api.add_resource(routes.Datasets, "/datasets/<string:id>")
    api.add_resource(routes.Concepts, "/concepts/<string:id>")
    api.add_resource(routes.DataServices, "/dataservices/<string:id>")

    return app
