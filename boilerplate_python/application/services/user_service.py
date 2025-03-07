from typing import Optional
from boilerplate_python.domain.user import User
from boilerplate_python.domain.interfaces.user_service_interface import IUserService
from boilerplate_python.domain.interfaces.user_repository_interface import IUserRepository
from boilerplate_python.application.use_cases.user.get_user_by_id_use_case import GetUserByIdUseCase 


class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):

        self.get_user_by_id_use_case = GetUserByIdUseCase(user_repository)

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        return self.get_user_by_id_use_case.execute(user_id)
