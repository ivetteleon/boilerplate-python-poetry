
"""
from boilerplate_python.application.settings import get_settings

from boilerplate_python.domain.schemas import SchemaTest
from boilerplate_python.domain.exceptions import OperationException

from boilerplate_python.application.interface_adapters.example_interface import IExampleGetDataUseCase

class Cli():
    __slots__ = ("logger", "example_get_data_use_ase")

    def __init__(self, example_get_data_use_ase: IExampleGetDataUseCase) -> None:

        self.logger = get_settings().general.logger()
        self.example_get_data_use_ase = example_get_data_use_ase


    def start(self) -> None:

        try:

            self.logger.set_context.set_context({"logging.googleapis.com/trace": f"projects/{get_settings().general.gcp_project_id}"})

            self.logger.get_context().info("START")
        
            data: SchemaTest = self.example_get_data_use_ase.execute()

            self.logger.get_context().info(f"data response -> {data}")
        
        
        except OperationException as opex:
            
            self.logger.get_context().error(f"Error: -> {opex.message}")

            """