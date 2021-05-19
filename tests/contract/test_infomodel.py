"""Test cases for information models."""
from typing import Any

import pytest
import requests


@pytest.mark.contract
def test_get_infomodel_with_id(http_service: Any) -> None:
    test_id = "6feff2b7-c7e5-3bde-99bf-9e5ae5cd6be8"
    url = f"{http_service}/information-models/{test_id}"
    result = requests.get(url=url, headers={"accept": "application/json"})
    parsed_result = result.json()

    assert parsed_result["identifier"] == [
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#AdresseModell"
    ]
    assert parsed_result["title"] == {"nb": "Vedens beste informasjonsmodell"}
    assert parsed_result["description"] == {
        "nb": "Overordnet informasjonsmodell for informasjon som kan kalles verdens beste"
    }
