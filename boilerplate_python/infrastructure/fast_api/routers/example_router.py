from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from boilerplate_python.infrastructure.fast_api.dependencies import get_use_cases

from boilerplate_python.infrastructure.services.example_service import ExampleService

from boilerplate_python.application.interface_adapters.example_interface import IExampleService
from boilerplate_python.application.interface_adapters.example_interface import IExampleService
from boilerplate_python.application.interface_adapters.example_interface import IExampleGetDataUseCase

router = APIRouter()

@router.post("/getSchemeTest")
def generate_auth_key(use_case: IExampleGetDataUseCase = Depends(get_use_cases("example_get_data_use_ase"))):

    data = use_case.execute()

    return data





