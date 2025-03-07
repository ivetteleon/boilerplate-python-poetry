from typing import Optional
from boilerplate_python.domain.interfaces.user_repository_interface import IUserRepository
from boilerplate_python.domain.user import User

class GetUserByIdUseCase():

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> Optional[User]:
        print("GET USER BY ID USE CASE", user_id)
        return self.user_repository.get_by_id(user_id)