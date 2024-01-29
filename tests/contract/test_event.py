"""Test cases for events."""

from typing import Any

import pytest
import requests


@pytest.mark.contract
def test_get_event_with_id(http_service: Any) -> None:
    test_id = "bc56fa1c-434a-3561-8fa7-e373dc1b6b55"

    url = f"{http_service}/events/{test_id}"
    result = requests.get(url=url, headers={"accept": "application/json"})

    assert result.headers["Cache-Control"] == "max-age=900"

    parsed_result = result.json()

    assert parsed_result["id"] == "bc56fa1c-434a-3561-8fa7-e373dc1b6b55"
    assert (
        parsed_result["uri"]
        == "http://public-service-publisher.fellesdatakatalog.digdir.no/events/ece8c4c0-2fa9-412a-a3fd-6eefe0681728"
    )
    assert parsed_result["identifier"] == "ece8c4c0-2fa9-412a-a3fd-6eefe0681728"
    assert parsed_result["title"]["nb"] == "Starte og drive restaurant"
    assert parsed_result["specialized_type"] == "business_event"
    assert parsed_result["dctType"][0]["prefLabel"]["nb"] == "Starte og drive bedrift"
