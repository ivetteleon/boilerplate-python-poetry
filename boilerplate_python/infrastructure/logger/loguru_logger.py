from __future__ import annotations

from loguru import logger

from abc import ABCMeta

from boilerplate_python.application.interface_adapters.logger_interface import ILogger

import datetime
import json
import loguru


class SingletonLoggerMeta(ABCMeta):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(ILogger, metaclass=SingletonLoggerMeta):

    def __init__(self):
        self._ctx = {}
        self._ctx_logger = None
        self._logger = logger
        self._logger.add(Logger.sink, backtrace=True, diagnose=True, level="INFO")

    @staticmethod
    def serialize(record: loguru.Record):
        subset = {
            "timestamp": record["time"]
            .utcnow()
            .replace(tzinfo=datetime.timezone.utc, microsecond=0)
            .isoformat(),
            "message": f'{record["name"]}:{record["function"]}:{record["line"]} - {record["message"]}',
            "severity": record["level"].name,
            "exception": str(record["exception"]),
            "elapsed": record["elapsed"].total_seconds(),
            **record["extra"],
        }
        return json.dumps(subset)

    @staticmethod
    def sink(message: loguru.Message):
        serialized = Logger.serialize(message.record)
        print(serialized)


    def set_context(self, ctx: dict):
        self._ctx = {**self._ctx, **ctx}
        self._ctx_logger = logger.bind(**self._ctx)


    def get_context(self):
        return self._ctx_logger if self._ctx_logger is not None else self._logger
    

    def info(self, message: str):
        self._logger.info(f"{message}")


    def warning(self, message: str):
        self._logger.warning(f"{message}")


    def error(self, message: str):
        self._logger.error(f"{message}")

