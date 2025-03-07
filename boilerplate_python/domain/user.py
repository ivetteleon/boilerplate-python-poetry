"""
User entity definition.
"""
from pydantic import BaseModel


class User(BaseModel):
    """User entity."""
    id: str
    email: str
    name: str
    is_active: bool = True