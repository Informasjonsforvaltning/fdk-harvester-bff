"""Test cases for concepts."""
from typing import Any

import pytest
import requests


@pytest.mark.contract
def test_get_data_service_with_id(http_service: Any) -> None:
    test_id = "a7562855-d02c-3681-8c52-c41dae1c8edc"
    url = f"{http_service}/dataservices/{test_id}"
    result = requests.get(url=url, headers={"accept": "application/json"})

    assert result.headers["Cache-Control"] == "max-age=900"

    parsed_result = result.json()

    assert parsed_result["id"] == test_id
    assert (
        parsed_result["uri"]
        == "https://dataservice-catalog.staging.fellesdatakatalog.digdir.no/data-services/5f5f33a8cbf97c1bd3bdd8f6"
    )
    assert parsed_result["title"] == {"nb": "National Data Directory Search API"}
    assert parsed_result["description"] == {
        "nb": "Provides a basic search api against the National Data Directory of Norway"
    }
    assert parsed_result["endpointDescription"] == [
        "https://raw.githubusercontent.com/brreg/openAPI/master/specs/fdk.json"
    ]
