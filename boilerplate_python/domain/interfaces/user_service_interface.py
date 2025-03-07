from abc import ABC, abstractmethod
from typing import Optional

from boilerplate_python.domain.user import User


class IUserService(ABC):
    """Interface for User Service operations."""

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass
