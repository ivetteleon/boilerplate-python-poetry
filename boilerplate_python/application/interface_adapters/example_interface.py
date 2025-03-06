from abc import ABCMeta
from abc import abstractmethod

from boilerplate_python.domain.responses import BaseServiceResponse
from boilerplate_python.domain.schemas import SchemaTest

from boilerplate_python.application.use_cases import BaseUseCase


# Define el tipo de dato que tendra data, el cual corresponde a la clase BaseServiceResponse, del cual se esta heredando.
class ExampleServiceResponse(BaseServiceResponse):

    data: SchemaTest | None


# Define la interfaz para un servicio
class IExampleService(metaclass=ABCMeta):

    @abstractmethod
    def get_test_result() -> ExampleServiceResponse:
        ...


# Define la interfaz para el caso de uso y se debe especificar el tipo de dato que retorna la funcion execute() que es parte de la clase BaseUseCase del cual esta heredando.
class IExampleGetDataUseCase(BaseUseCase):

    def execute(self) -> SchemaTest:
        ...