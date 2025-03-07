"""
from boilerplate_python.domain.schemas import SchemaTest

from boilerplate_python.application.example.use_cases.example_use_case import ExampleGetDataUseCase

from boilerplate_python.application.interface_adapters.example_interface import ExampleServiceResponse

from boilerplate_python.infrastructure.services.example_service import ExampleService
from boilerplate_python.infrastructure.logger.loguru_logger import Logger


def test_get_data():

    logger_instance = Logger()
    logger_instance.set_context({"logging.googleapis.com/trace": f"projects/PROJECT_ID/traces/TRACE[0]"})

    example_service = ExampleService()

    example_use_case = ExampleGetDataUseCase(example_service)

    data = example_use_case.execute()

    assert isinstance(data, SchemaTest)
    
"""