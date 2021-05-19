"""Test cases for concepts."""
from typing import Any

import pytest
import requests


@pytest.mark.contract
def test_get_concept_with_id(http_service: Any) -> None:
    test_id = "a683bc63-2961-46af-9956-8a4a3f991cc6"
    url = f"{http_service}/concepts/{test_id}"
    result = requests.get(url=url, headers={"accept": "application/json"})
    parsed_result = result.json()

    assert parsed_result["id"] == "a683bc63-2961-46af-9956-8a4a3f991cc6"
    assert (
        parsed_result["identifier"]
        == "http://begrepskatalogen/begrep/88804c36-ff43-11e6-9d97-005056825ca0"
    )
    assert parsed_result["prefLabel"] == {"nb": "norsk etternavn"}
    assert parsed_result["altLabel"] == [{"nb": "etternavn"}]
    assert parsed_result["definition"]["text"] == {
        "nb": "navn som i rekkefølge er etter fornavn og eventuelt mellomnavn  som skal være i henhold til Lov om personnavn"
    }
    assert parsed_result["definition"]["remark"] == {
        "nb": "Kan være bygget opp av to etternavn satt sammen med bindestrek - såkalt dobbelt etternavn. For at et navn skal anses som navn etter navneloven, må det i utgangspunktet være uttrykt med bokstavene i det norske alfabetet med de diakritiske tegn som støttes av folkeregisteret"
    }
