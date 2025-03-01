from enum import Enum
from typing import Any, Type, Optional

from pydantic import BaseModel
from pydantic import Field


class SchemaTest(BaseModel):

    id: str
    name: str
    
