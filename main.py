from boilerplate_python.application.use_cases.example_use_case import ExampleGetDataUseCase

from boilerplate_python.infrastructure.services.example_service import ExampleService

from boilerplate_python.infrastructure.triggers.cli import Cli
from boilerplate_python.infrastructure.fast_api.executor import FastApi

def handler() -> None:

    # Instanciar la implementacion de los servicios correspondientes.
    example_service = ExampleService()

    # Crear la instancia de los casos de uso con la implementacion de los servicios correspondientes.
    example_get_data_use_case = ExampleGetDataUseCase(example_service)

    fast_api = FastApi(example_get_data_use_case)
    fast_api.start()

    #cli = Cli(example_get_data_use_case)
    #cli.start()


if __name__ == "__main__":  

    handler()
