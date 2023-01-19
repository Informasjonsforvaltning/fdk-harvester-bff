from typing import Any

from flask import Response
from flask_restful import Resource
import simplejson as json

from fdk_harvester_bff.service.services import (
    FetchFromServiceException,
    get_concept_by_id,
    get_data_service_by_id,
    get_dataset_by_id,
    get_event_by_id,
    get_information_model_by_id,
    get_public_service_by_id,
)

_cache_control_one_day = {"Cache-Control": "max-age=900"}


class Ping(Resource):
    """Ping resource."""

    def get(self: Any) -> Response:
        """Ping route function."""
        return Response(status=200)


class Ready(Resource):
    """Ready resource."""

    def get(self: Any) -> Response:
        """Ready route function."""
        return Response(status=200)


class InfoModels(Resource):
    """Information models resource."""

    def get(self: Any, id: str) -> Response:
        """Get information model by id."""
        try:
            body = json.dumps(get_information_model_by_id(id), iterable_as_array=True)
            response = Response(body, status=200, content_type="application/json")
            response.headers.extend(_cache_control_one_day)
            return response
        except FetchFromServiceException as err:
            return Response(status=err.status)


class Datasets(Resource):
    """Datasets resource."""

    def get(self: Any, id: str) -> Response:
        """Get dataset by id."""
        try:
            body = json.dumps(get_dataset_by_id(id), iterable_as_array=True)
            response = Response(body, status=200, content_type="application/json")
            response.headers.extend(_cache_control_one_day)
            return response
        except FetchFromServiceException as err:
            return Response(err.reason, status=err.status)


class Concepts(Resource):
    """Concepts resource."""

    def get(self: Any, id: str) -> Response:
        """Get concept by id."""
        try:
            body = json.dumps(get_concept_by_id(id), iterable_as_array=True)
            response = Response(body, status=200, content_type="application/json")
            response.headers.extend(_cache_control_one_day)
            return response
        except FetchFromServiceException as err:
            return Response(err.reason, status=err.status)


class DataServices(Resource):
    """Data services resource."""

    def get(self: Any, id: str) -> Response:
        """Get data service by id."""
        try:
            body = json.dumps(get_data_service_by_id(id), iterable_as_array=True)
            response = Response(body, status=200, content_type="application/json")
            response.headers.extend(_cache_control_one_day)
            return response
        except FetchFromServiceException as err:
            return Response(err.reason, status=err.status)


class Events(Resource):
    """Events resource."""

    def get(self: Any, id: str) -> Response:
        """Get Event by id."""
        try:
            body = json.dumps(get_event_by_id(id), iterable_as_array=True)
            response = Response(body, status=200, content_type="application/json")
            response.headers.extend(_cache_control_one_day)
            return response
        except FetchFromServiceException as err:
            return Response(err.reason, status=err.status)


class PublicServices(Resource):
    """Public services resource."""

    def get(self: Any, id: str) -> Response:
        """Get public service by id."""
        try:
            body = json.dumps(get_public_service_by_id(id), iterable_as_array=True)
            response = Response(body, status=200, content_type="application/json")
            response.headers.extend(_cache_control_one_day)
            return response
        except FetchFromServiceException as err:
            return Response(err.reason, status=err.status)
