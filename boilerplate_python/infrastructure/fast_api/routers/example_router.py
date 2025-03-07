from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from boilerplate_python.domain.interfaces.user_service_interface import IUserService
from boilerplate_python.infrastructure.fast_api.dependencies import get_use_cases

router = APIRouter()

"""
@router.post("/getSchemeTest")
def generate_auth_key(use_case: IExampleGetDataUseCase = Depends(get_use_cases("example_get_data_use_ase"))):

    data = use_case.execute()

    return data

    """

@router.get("/users/{user_id}")
async def get_user(user_id: str, user_service: IUserService = Depends(get_use_cases("user_service"))):
    return user_service.get_user_by_id(user_id)


