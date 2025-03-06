from enum import Enum
from typing import Any, Type, Optional

from pydantic import BaseModel
from pydantic import Field


class StatusResponse(str, Enum):

    SUCCESS = "success"
    FAILURE = "failure"
    ERROR = "error"


class BaseServiceResponse(BaseModel):

    data: BaseModel
    code: int | None
    message: str | None
    status: StatusResponse = StatusResponse.SUCCESS


