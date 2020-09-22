# (generated with --quick)

import os
from typing import Any, Union

logger_class = CustomGunicornLogger

DEBUG_MODE: Union[bool, str]
LOG_LEVEL: str
PORT: str
accesslog: str
bind: str
env: os._Environ[str]
glogging: Any
load_dotenv: Any
logging: module
loglevel: str
multiprocessing: module
threads: int
workers: int

class CustomGunicornLogger(Any):
    __doc__: str
    def setup(self, cfg) -> None: ...

class PingFilter(logging.Filter):
    __doc__: str
    def filter(self, record: logging.LogRecord) -> bool: ...

class ReadyFilter(logging.Filter):
    __doc__: str
    def filter(self, record: logging.LogRecord) -> bool: ...
