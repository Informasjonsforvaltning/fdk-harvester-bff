# (generated with --quick)

import fdk_harvester_bff.service.services
import flask.app
import flask.wrappers
from typing import Any, Iterable, NoReturn, Type, Union
import werkzeug.wrappers

FetchFromServiceException: Type[fdk_harvester_bff.service.services.FetchFromServiceException]
Flask: Type[flask.app.Flask]
Response: Type[flask.wrappers.Response]
json: module
load_dotenv: Any
request: flask.wrappers.Request

def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
def create_app(test_config = ...) -> flask.app.Flask: ...
def get_dataset_by_id(id: str) -> Any: ...
def jsonify(*args, **kwargs) -> Any: ...
def make_response(*args) -> flask.wrappers.Response: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
