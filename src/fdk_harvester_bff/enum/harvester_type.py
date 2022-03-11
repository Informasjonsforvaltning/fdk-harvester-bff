from enum import Enum


class HarvesterType(Enum):

    DATASET = "dataset"
    DATA_SERVICE = "dataservice"
    CONCEPT = "concept"
    INFO_MODEL = "informationmodel"
    EVENT = "event"
    PUBLIC_SERVICE = "publicservice"
