from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import datetime

from boilerplate_python.domain.user import User

class IUserRepository(ABC):
    """Interface for User Repository operations."""
    
    @abstractmethod
    async def get_by_id(self, user_id: str) -> Optional[User]:
        """Get a user by their ID.
        
        Args:
            user_id: The unique identifier of the user
            
        Returns:
            Optional[User]: User data if found, None otherwise
        """
        pass
    