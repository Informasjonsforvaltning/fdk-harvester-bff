from dataclasses import asdict
from os import environ as env
from typing import Any

from fdk_rdf_parser import parse_concepts, parse_datasets, parse_information_models
from requests import get, HTTPError

INFORMATION_MODEL_HARVESTER_BASE_URL = env.get(
    "INFORMATION_MODEL_HARVESTER_BASE_URL", "http://localhost:8000"
)
DATASET_HARVESTER_BASE_URL = env.get(
    "DATASET_HARVESTER_BASE_URL", "http://localhost:8000"
)
CONCEPT_HARVESTER_BASE_URL = env.get(
    "CONCEPT_HARVESTER_BASE_URL", "http://localhost:8000"
)
RECORDS_PARAM_TRUE = {"catalogrecords": "true"}


def get_information_model_by_id(id: str) -> Any:
    url = f"{INFORMATION_MODEL_HARVESTER_BASE_URL}/informationmodels/{id}"
    try:
        req = get(
            url=url,
            params=RECORDS_PARAM_TRUE,
            headers={"Accept": "text/turtle"},
            timeout=5,
        )

        if req.status_code == 404:
            raise FetchFromServiceException(
                status=404, reason=f"No information model with {id} found"
            )
        req.raise_for_status()

        parsed_information_model = parse_information_models(req.text)
        if parsed_information_model is None or len(parsed_information_model) != 1:
            raise FetchFromServiceException(
                status=500,
                reason=f"Error when attempting to parse dataset with id {id}",
            )
        return asdict(
            parsed_information_model.get(list(parsed_information_model.keys())[0])
        )
    except HTTPError as err:
        raise FetchFromServiceException(status=500, reason=err.strerror)
    except (ConnectionError, TimeoutError) as err:
        raise FetchFromServiceException(status=502, reason=err.strerror)


def get_dataset_by_id(id: str) -> Any:
    url = f"{DATASET_HARVESTER_BASE_URL}/datasets/{id}"
    try:
        req = get(
            url=url,
            params=RECORDS_PARAM_TRUE,
            headers={"Accept": "text/turtle"},
            timeout=5,
        )

        if req.status_code == 404:
            raise FetchFromServiceException(
                status=404, reason=f"No dataset with {id} found"
            )
        req.raise_for_status()

        parsed_dataset = parse_datasets(req.text)
        if parsed_dataset is None or len(parsed_dataset) != 1:
            raise FetchFromServiceException(
                status=500,
                reason=f"Error when attempting to parse dataset with id {id}",
            )
        return asdict(parsed_dataset.get(list(parsed_dataset.keys())[0]))
    except HTTPError as err:
        raise FetchFromServiceException(status=500, reason=err.strerror)
    except (ConnectionError, TimeoutError) as err:
        raise FetchFromServiceException(status=502, reason=err.strerror)


def get_concept_by_id(id: str) -> Any:
    url = f"{CONCEPT_HARVESTER_BASE_URL}/concepts/{id}"
    try:
        req = get(
            url=url,
            params=RECORDS_PARAM_TRUE,
            headers={"Accept": "text/turtle"},
            timeout=5,
        )

        if req.status_code == 404:
            raise FetchFromServiceException(
                status=404, reason=f"No concept with {id} found"
            )
        req.raise_for_status()

        parsed_dataset = parse_concepts(req.text)
        if parsed_dataset is None or len(parsed_dataset) != 1:
            raise FetchFromServiceException(
                status=500,
                reason=f"Error when attempting to parse concept with id {id}",
            )
        return asdict(parsed_dataset.get(list(parsed_dataset.keys())[0]))
    except HTTPError as err:
        raise FetchFromServiceException(status=500, reason=err.strerror)
    except (ConnectionError, TimeoutError) as err:
        raise FetchFromServiceException(status=502, reason=err.strerror)


class FetchFromServiceException(BaseException):
    __slots__ = ("status", "reason")

    def __init__(self, status: int, reason: str) -> None:
        self.status = status
        self.reason = reason
