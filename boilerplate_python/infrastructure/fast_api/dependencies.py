from typing import Callable

from boilerplate_python.application.interface_adapters.example_interface import IExampleGetDataUseCase


example_get_data_use_ase: IExampleGetDataUseCase = None


def set_use_cases(example_use_case_imp: IExampleGetDataUseCase):

    global example_get_data_use_ase
    example_get_data_use_ase = example_use_case_imp


def get_use_cases(_type: str) -> Callable:

    return {
        "example_get_data_use_ase": lambda: example_get_data_use_ase
    }.get(_type)
