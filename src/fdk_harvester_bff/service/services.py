from dataclasses import asdict
from os import environ as env
from typing import Any

from fdk_rdf_parser import (
    parse_concepts,
    parse_data_services,
    parse_datasets,
    parse_information_models,
)
from requests import get, HTTPError

from fdk_harvester_bff.enum.harvester_type import HarvesterType

INFORMATION_MODEL_HARVESTER_BASE_URL = env.get(
    "INFORMATION_MODEL_HARVESTER_BASE_URL", "http://localhost:8000"
)
DATASET_HARVESTER_BASE_URL = env.get(
    "DATASET_HARVESTER_BASE_URL", "http://localhost:8000"
)
CONCEPT_HARVESTER_BASE_URL = env.get(
    "CONCEPT_HARVESTER_BASE_URL", "http://localhost:8000"
)
DATA_SERVICE_HARVESTER_BASE_URL = env.get(
    "DATA_SERVICE_HARVESTER_BASE_URL", "http://localhost:8000"
)
RECORDS_PARAM_TRUE = {"catalogrecords": "true"}


def get_information_model_by_id(id: str) -> Any:
    return _get_and_parse_rdf_from_harvester(id, HarvesterType.INFO_MODEL)


def get_dataset_by_id(id: str) -> Any:
    return _get_and_parse_rdf_from_harvester(id, HarvesterType.DATASET)


def get_concept_by_id(id: str) -> Any:
    return _get_and_parse_rdf_from_harvester(id, HarvesterType.CONCEPT)


def get_data_service_by_id(id: str) -> Any:
    return _get_and_parse_rdf_from_harvester(id, HarvesterType.DATA_SERVICE)


def _get_and_parse_rdf_from_harvester(id: str, type: HarvesterType) -> Any:
    url = _harvester_url(id, type)
    try:
        req = get(
            url=url,
            params=RECORDS_PARAM_TRUE,
            headers={"Accept": "text/turtle"},
            timeout=5,
        )

        if req.status_code == 404:
            raise FetchFromServiceException(
                status=404, reason=f"No {type.value} with {id} found"
            )
        req.raise_for_status()

        parsed = _parse_rdf(req.text, type)
        if parsed is None or len(parsed) != 1:
            raise FetchFromServiceException(
                status=500,
                reason=f"Error when attempting to parse {type.value} with id {id}",
            )
        return asdict(parsed.get(list(parsed.keys())[0]))
    except HTTPError as err:
        raise FetchFromServiceException(status=500, reason=err.strerror) from None
    except (ConnectionError, TimeoutError) as err:
        raise FetchFromServiceException(status=502, reason=err.strerror) from None


def _harvester_url(id: str, type: HarvesterType) -> Any:
    if type == HarvesterType.CONCEPT:
        return f"{CONCEPT_HARVESTER_BASE_URL}/concepts/{id}"
    elif type == HarvesterType.DATA_SERVICE:
        return f"{DATA_SERVICE_HARVESTER_BASE_URL}/dataservices/{id}"
    elif type == HarvesterType.DATASET:
        return f"{DATASET_HARVESTER_BASE_URL}/datasets/{id}"
    elif type == HarvesterType.INFO_MODEL:
        return f"{INFORMATION_MODEL_HARVESTER_BASE_URL}/informationmodels/{id}"


def _parse_rdf(rdf: str, type: HarvesterType) -> Any:
    if type == HarvesterType.CONCEPT:
        return parse_concepts(rdf)
    elif type == HarvesterType.DATA_SERVICE:
        return parse_data_services(rdf)
    elif type == HarvesterType.DATASET:
        return parse_datasets(rdf)
    elif type == HarvesterType.INFO_MODEL:
        return parse_information_models(rdf)


class FetchFromServiceException(BaseException):
    __slots__ = ("status", "reason")

    def __init__(self, status: int, reason: str) -> None:
        self.status = status
        self.reason = reason
