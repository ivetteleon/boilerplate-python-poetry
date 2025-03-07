
"""
from boilerplate_python.application.interface_adapters.example_interface import ExampleServiceResponse
from boilerplate_python.application.interface_adapters.example_interface import IExampleService

from boilerplate_python.infrastructure.logger.loguru_logger import Logger
from boilerplate_python.application.settings import get_settings

from boilerplate_python.domain.responses import StatusResponse
from boilerplate_python.domain.schemas import SchemaTest


class ExampleService(IExampleService):
    __slots__ = ("logger")


    def __init__(self):

        self.logger = get_settings().general.logger()
        
    
    def get_test_result(self) -> ExampleServiceResponse:

        self.logger.get_context().info("START")

        obj = SchemaTest.parse_obj(
            {
                "id": "123456",
                "name": "Nombre Objeto"
            }
        )

        return ExampleServiceResponse(
            status = StatusResponse.SUCCESS,
            code=200,
            data = obj
        )
"""