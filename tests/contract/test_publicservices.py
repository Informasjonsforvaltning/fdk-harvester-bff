"""Test cases for events."""
from typing import Any

import pytest
import requests


@pytest.mark.contract
def test_get_public_service_with_id(http_service: Any) -> None:
    test_id = "536bfa22-0126-3032-b31a-af8d05b7b0ae"

    url = f"{http_service}/public-services/{test_id}"
    result = requests.get(url=url, headers={"accept": "application/json"})

    assert result.headers["Cache-Control"] == "max-age=900"

    parsed_result = result.json()

    assert parsed_result["id"] == "536bfa22-0126-3032-b31a-af8d05b7b0ae"
    assert (
        parsed_result["uri"]
        == "http://public-service-publisher.fellesdatakatalog.digdir.no/services/9"
    )
    assert parsed_result["identifier"] == "9"
    assert parsed_result["title"]["nb"] == "Søknad om internasjonal grunnstøtte"
