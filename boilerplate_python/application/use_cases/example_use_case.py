
from boilerplate_python.application.settings import get_settings

from boilerplate_python.application.use_cases import BaseUseCase

from boilerplate_python.application.interface_adapters.example_interface import ExampleServiceResponse
from boilerplate_python.application.interface_adapters.example_interface import IExampleService
from boilerplate_python.application.interface_adapters.example_interface import IExampleGetDataUseCase

from boilerplate_python.domain.schemas import SchemaTest
from boilerplate_python.domain.exceptions import OperationException


class ExampleGetDataUseCase(IExampleGetDataUseCase):

    __slots__ = ("logger", "example_service")
    
    def __init__(self, example_service: IExampleService) -> None:
        
        self.logger = get_settings().general.logger()
        self.example_service = example_service


    def execute(self) -> SchemaTest:

        self.logger.get_context().info("START")

        response: ExampleServiceResponse = self.example_service.get_test_result()

        self.logger.get_context().info(f"response -> {response}")

        if(response.code == 200):

            return response.data
        
        else:

            self.logger.get_context().error(f"ExampleServiceResponse Error: {response.message}")

            raise OperationException(
                code=500, message=f"{response.message}", function="get_data", obj="ExampleGetDataUseCase"
            )
        