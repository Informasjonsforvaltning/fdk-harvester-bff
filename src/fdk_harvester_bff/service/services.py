from dataclasses import asdict
from os import environ as env
from typing import Any

from fdk_rdf_parser import parseDatasets
from requests import get, HTTPError


def get_dataset_by_id(id: str) -> Any:
    base_url = env.get(
        "DATASET_HARVESTER_BASE_URL",
        "http://localhost:8000",
    )
    url = f"{base_url}/datasets/{id}"
    try:
        req = get(url=url, headers={"Accept": "text/turtle"}, timeout=5)

        if req.status_code == 404:
            raise FetchFromServiceException(
                status=404, message=f"No dataset with {id} found"
            )
        req.raise_for_status()

        parsed_dataset = parseDatasets(req.text)
        if parsed_dataset is None or len(parsed_dataset) != 1:
            raise FetchFromServiceException(
                status=500,
                message=f"Error when attempting to parse dataset with id {id}",
            )
        return asdict(parsed_dataset.get(list(parsed_dataset.keys())[0]))
    except HTTPError as err:
        raise FetchFromServiceException(status=500, message=err.strerror)
    except (ConnectionError, TimeoutError) as err:
        raise FetchFromServiceException(status=502, message=err.strerror)


class FetchFromServiceException(BaseException):
    __slots__ = ("status", "message")

    def __init__(self, status: int, message: str) -> None:
        self.status = status
        self.message = message
