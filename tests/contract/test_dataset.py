"""Test cases for datasets."""
from typing import Any

import pytest
import requests


@pytest.mark.contract
def test_get_dataset_with_id(http_service: Any) -> None:
    expected = {
        "publisher": {
            "uri": "https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/971526920",
            "id": None,
            "name": None,
            "orgPath": "/STAT/972417807/971526920",
            "prefLabel": {"nb": "STATISTISK SENTRALBYRÅ"},
            "organisasjonsform": None,
        },
        "title": {"nb": "Fylkesinndeling"},
        "description": {
            "nb": "Datasettet inneholder tosifret fylkeskode og offisielt navn på fylke. "
            "Fylkene er regionale administrative enheter både for statlig og fylkeskommunal virksomhet."
        },
        "descriptionFormatted": {
            "nb": "Datasettet inneholder tosifret fylkeskode og offisielt navn på fylke. Fylkene er"
            " regionale administrative enheter både for statlig og fylkeskommunal virksomhet."
        },
        "uri": "https://data.norge.no/node/1113",
        "accessRights": {
            "uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
            "code": "PUBLIC",
            "prefLabel": None,
        },
        "theme": [
            {
                "id": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
                "code": "GOVE",
                "startUse": "2015-10-01",
                "title": {
                    "it": "Governo e settore pubblico",
                    "nb": "Forvaltning og offentlig sektor",
                    "en": "Government and public sector",
                    "hr": "Vlada i javni sektor",
                    "es": "Gobierno y sector público",
                    "de": "Regierung und öffentlicher Sektor",
                    "sk": "Vláda a verejný sektor",
                    "ro": "Guvern şi sector public",
                    "bg": "Правителство и публичен сектор",
                    "et": "Valitsus ja avalik sektor",
                    "el": "Κυβέρνηση και δημόσιος τομέας",
                    "pl": "Rząd i sektor publiczny",
                    "cs": "Vláda a veřejný sektor",
                    "ga": "Rialtas agus earnáil phoiblí",
                    "pt": "Governo e setor público",
                    "lt": "Vyriausybė ir viešasis sektorius",
                    "lv": "Valdība un sabiedriskais sektors",
                    "mt": "Gvern u settur pubbliku",
                    "hu": "Kormányzat és közszféra",
                    "da": "Regeringen og den offentlige sektor",
                    "fi": "Valtioneuvosto ja julkinen sektori",
                    "fr": "Gouvernement et secteur public",
                    "sl": "Vlada in javni sektor",
                    "sv": "Regeringen och den offentliga sektorn",
                    "nl": "Overheid en publieke sector",
                },
                "conceptSchema": {
                    "id": "http://publications.europa.eu/resource/authority/data-theme",
                    "title": {"en": "Dataset types Named Authority List"},
                    "versioninfo": "20160921-0",
                    "versionnumber": "20160921-0",
                },
            },
            {
                "id": "http://publications.europa.eu/resource/authority/data-theme/REGI",
                "code": "REGI",
                "startUse": "2015-10-01",
                "title": {
                    "hr": "Regije i gradovi",
                    "en": "Regions and cities",
                    "nb": "Regioner og byer",
                    "da": "Regioner og byer",
                    "es": "Regiones y ciudades",
                    "sl": "Regije in mesta",
                    "lv": "Reģioni un pilsētas",
                    "it": "Regioni e città",
                    "el": "Περιφέρειες και πόλεις",
                    "de": "Regionen und Städte",
                    "hu": "Régiók és városok",
                    "ro": "Regiuni şi orașe",
                    "ga": "Réigiúin agus cathracha",
                    "fi": "Alueet ja kaupungit",
                    "et": "Piirkonnad ja linnad",
                    "pt": "Regiões e cidades",
                    "fr": "Régions et villes",
                    "pl": "Regiony i miasta",
                    "lt": "Regionai ir miestai",
                    "sv": "Regioner och städer",
                    "nl": "Regio's en steden",
                    "bg": "Региони и градове",
                    "cs": "Regiony a města",
                    "sk": "Regióny a mestá",
                    "mt": "Reġjuni u bliet",
                },
                "conceptSchema": {
                    "id": "http://publications.europa.eu/resource/authority/data-theme",
                    "title": {"en": "Dataset types Named Authority List"},
                    "versioninfo": "20160921-0",
                    "versionnumber": "20160921-0",
                },
            },
        ],
        "keyword": [
            {"nb": "standard"},
            {"nb": "fylkeskode"},
            {"nb": "fylke"},
            {"nb": "fylkesnummer"},
            {"nb": "regionale enheter"},
        ],
        "contactPoint": [
            {
                "uri": None,
                "fullname": None,
                "email": "statistikkbanken@ssb.no",
                "organizationName": None,
                "organizationUnit": None,
                "hasURL": None,
                "hasTelephone": None,
            }
        ],
        "type": "datasets",
        "dctType": "Kodelister",
        "issued": "2014-10-15T14:10:00",
        "modified": "2020-01-01",
        "landingPage": ["https://www.ssb.no/klass/klassifikasjoner/104"],
        "language": [
            {
                "uri": "http://publications.europa.eu/resource/authority/language/NOR",
                "code": "NOR",
                "prefLabel": {
                    "nb": "Norsk",
                    "nn": "Norsk",
                    "no": "Norsk",
                    "en": "Norwegian",
                },
            }
        ],
        "id": "dd05acaa-1c89-4139-8612-0ad10e75d6a6",
        "harvest": {
            "firstHarvested": "2017-12-19T15:58:36Z",
            "changed": ["2020-08-05T01:13:59Z"],
        },
        "accessRightsComment": None,
        "distribution": [
            {
                "uri": None,
                "title": None,
                "description": {"nb": "Webside og nedlastbar CSV-fil"},
                "downloadURL": ["https://data.ssb.no/api/klass/v1/versions/1158.csv"],
                "accessURL": ["https://www.ssb.no/klass/klassifikasjoner/104"],
                "license": None,
                "openLicense": False,
                "conformsTo": None,
                "page": None,
                "format": ["CSV", "HTML"],
                "type": None,
                "accessService": None,
            },
            {
                "uri": None,
                "title": None,
                "description": {"nb": "REST-API i formatene XML og JSON"},
                "downloadURL": ["https://data.ssb.no/api/klass/v1/versions/916.xml"],
                "accessURL": ["https://data.ssb.no/api/klass/v1/api-guide.html"],
                "license": None,
                "openLicense": False,
                "conformsTo": None,
                "page": None,
                "format": ["XML"],
                "type": None,
                "accessService": None,
            },
            {
                "uri": None,
                "title": {"nb": "REST-API i formatene XML og JSON"},
                "description": None,
                "downloadURL": ["https://data.ssb.no/api/klass/v1/versions/1158.json"],
                "accessURL": ["https://data.ssb.no/api/klass/v1/api-guide.html"],
                "license": [
                    {
                        "uri": "http://data.norge.no/nlod/",
                        "prefLabel": {
                            "no": "Norsk lisens for offentlige data",
                            "en": "Norwegian Licence for Open Government Data",
                        },
                        "extraType": "http://purl.org/dc/terms/LicenseDocument",
                    }
                ],
                "openLicense": False,
                "conformsTo": None,
                "page": None,
                "format": ["JSON"],
                "type": None,
                "accessService": None,
            },
        ],
        "sample": None,
        "source": None,
        "objective": None,
        "page": None,
        "admsIdentifier": None,
        "temporal": None,
        "subject": None,
        "spatial": [
            {
                "uri": "https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
                "code": "https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
                "prefLabel": {"no": "Norge"},
            }
        ],
        "provenance": {
            "uri": "http://data.brreg.no/datakatalog/provinens/nasjonal",
            "code": "NASJONAL",
            "prefLabel": {
                "en": "Authoritativ source",
                "nb": "Autoritativ kilde",
                "nn": "Autoritativ kilde",
            },
        },
        "accrualPeriodicity": {
            "uri": "http://publications.europa.eu/resource/authority/frequency/IRREG",
            "code": "IRREG",
            "prefLabel": {
                "mt": "irregolari",
                "hu": "rendszertelen",
                "es": "irregular",
                "en": "irregular",
                "pt": "irregular",
                "cs": "nepravidelný",
                "sk": "nepravidelný",
                "bg": "неправилен",
                "sv": "oregelbundet",
                "el": "μη τακτικός",
                "no": "uregelmessig",
                "da": "uregelmæssigt",
                "fr": "irrégulier",
                "ro": "neregulat",
                "lt": "nereguliarus",
                "et": "ebakorrapärane",
                "fi": "epäsäännöllinen",
                "pl": "nieregularny",
                "hr": "neredovit",
                "it": "irregolare",
                "lv": "neregulāri",
                "sl": "nepravilen",
                "ga": "neamhrialta",
                "nl": "onregelmatig",
                "de": "unregelmäßig",
            },
        },
        "hasCurrentnessAnnotation": {
            "inDimension": "http://iso.org/25012/2008/dataquality/Currentness",
            "hasBody": None,
        },
        "losTheme": [
            {
                "children": [
                    "https://psi.norge.no/los/tema/priser-og-gebyr-for-bygg-og-eiendom",
                    "https://psi.norge.no/los/tema/bygging",
                    "https://psi.norge.no/los/tema/leie-og-utleie",
                    "https://psi.norge.no/los/tema/planer",
                    "https://psi.norge.no/los/tema/kjop-og-salg",
                    "https://psi.norge.no/los/tema/flytting",
                    "https://psi.norge.no/los/tema/eiendom",
                ],
                "parents": None,
                "isTema": True,
                "losPaths": ["bygg-og-eiendom"],
                "name": {
                    "nn": "Bygg og eigedom",
                    "nb": "Bygg og eiendom",
                    "en": "Building and property",
                },
                "definition": None,
                "uri": "https://psi.norge.no/los/tema/bygg-og-eiendom",
                "synonyms": [],
                "relatedTerms": None,
            },
            {
                "children": [
                    "https://psi.norge.no/los/tema/tilskuddsordninger-for-naring",
                    "https://psi.norge.no/los/tema/naringsliv",
                    "https://psi.norge.no/los/tema/naringsutvikling",
                    "https://psi.norge.no/los/tema/landbruk",
                    "https://psi.norge.no/los/tema/handel-og-service",
                ],
                "parents": None,
                "isTema": True,
                "losPaths": ["naring"],
                "name": {"nn": "Næring", "nb": "Næring", "en": "Business"},
                "definition": None,
                "uri": "https://psi.norge.no/los/tema/naring",
                "synonyms": [],
                "relatedTerms": None,
            },
        ],
    }
    test_id = "dd05acaa-1c89-4139-8612-0ad10e75d6a6"
    url = f"{http_service}/datasets/{test_id}"
    result = requests.get(url=url, headers={"accept": "application/json"})

    assert result.headers["Cache-Control"] == "max-age=86400"

    parsed_dataset = result.json()
    assert (
        parsed_dataset["publisher"]["prefLabel"]["nb"]
        == expected["publisher"]["prefLabel"]["nb"]  # type: ignore
    )
    assert parsed_dataset["title"] == expected["title"]
    assert parsed_dataset["description"] == expected["description"]
    assert parsed_dataset["uri"] == expected["uri"]
    assert parsed_dataset["accessRights"] == expected["accessRights"]
    dataset_themes = [theme["code"] for theme in parsed_dataset["theme"]]
    assert len(dataset_themes) == 2
    assert "GOVE" in dataset_themes
    assert "REGI" in dataset_themes
    assert set([word["nb"] for word in parsed_dataset["keyword"]]) == set(
        [word["nb"] for word in expected["keyword"]]  # type: ignore
    )
    assert parsed_dataset["type"] == expected["type"]
    flat_parsed_dist = []
    for dist in [dist["downloadURL"] for dist in parsed_dataset["distribution"]]:
        flat_parsed_dist.extend(dist)
    flat_expected_dist = []
    for dist in [dist["downloadURL"] for dist in expected["distribution"]]:  # type: ignore
        flat_expected_dist.extend(dist)
    assert set(flat_parsed_dist) == set(flat_expected_dist)
    assert parsed_dataset["spatial"] == expected["spatial"]
    assert parsed_dataset["losTheme"] == expected["losTheme"]
    assert parsed_dataset["provenance"] == expected["provenance"]
