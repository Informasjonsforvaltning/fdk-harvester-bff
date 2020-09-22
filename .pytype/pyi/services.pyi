# (generated with --quick)

import os
import requests.exceptions
import requests.models
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Tuple, Type, TypeVar, Union

HTTPError: Type[requests.exceptions.HTTPError]
env: os._Environ[str]
parseDatasets: Any

_T = TypeVar('_T')

class FetchFromServiceException(BaseException):
    __slots__ = ["message", "status"]
    message: str
    status: int
    def __init__(self, status: int, message: str) -> None: ...

@overload
def asdict(obj) -> Dict[str, Any]: ...
@overload
def asdict(obj, *, dict_factory: Callable[[List[Tuple[str, Any]]], _T]) -> _T: ...
def get(url: Union[bytes, str], params: Optional[Union[bytes, str, Mapping[Union[bytes, float, str], Union[bytes, float, str, Iterable[Union[bytes, float, str]]]], Tuple[Union[bytes, float, str], Union[bytes, float, str, Iterable[Union[bytes, float, str]]]]]] = ..., **kwargs) -> requests.models.Response: ...
def get_dataset_by_id(id: str) -> Any: ...
