from typing import Any

from flask import Response
from flask_restful import Resource
import simplejson as json

from fdk_harvester_bff.service.services import (
    FetchFromServiceException,
    get_dataset_by_id,
    get_information_model_by_id,
)


class Ping(Resource):
    """Ping."""

    def get(self: Any) -> Response:
        """Ping route function."""
        return Response(status=200)


class Ready(Resource):
    """Ready."""

    def get(self: Any) -> Response:
        """Ready route function."""
        return Response(status=200)


class InfoModels(Resource):
    """Information models resource."""

    def get(self: Any, id: str) -> Response:
        """Get information model by id."""
        try:
            body = json.dumps(get_information_model_by_id(id), iterable_as_array=True)
            return Response(body, status=200, content_type="application/json")
        except FetchFromServiceException as err:
            return Response(status=err.status)


class Datasets(Resource):
    """Datasets resource."""

    def get(self: Any, id: str) -> Response:
        """Get dataset by id."""
        try:
            body = json.dumps(get_dataset_by_id(id), iterable_as_array=True)
            return Response(body, status=200, content_type="application/json")
        except FetchFromServiceException as err:
            return Response(err.reason, status=err.status)
