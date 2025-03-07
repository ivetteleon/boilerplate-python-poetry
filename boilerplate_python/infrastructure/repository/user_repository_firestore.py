from typing import List, Optional, Dict, Any
from datetime import datetime
from boilerplate_python.domain.interfaces.user_repository_interface import IUserRepository
from boilerplate_python.domain.user import User

class UserRepositoryFirestore(IUserRepository):
    """Simple in-memory implementation of User Repository."""
    
    def __init__(self):
        self._users: Dict[str, Dict[str, Any]] = {}
    
    
    def get_by_id(self, user_id: str) -> Optional[User]:
        """Get a user by their ID."""
        user = User(
            id=user_id,
            name="John Doe",
            email="john.doe@example.com",
            is_active=True
        )
        return user