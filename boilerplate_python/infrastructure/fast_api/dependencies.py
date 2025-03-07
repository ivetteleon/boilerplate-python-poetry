from typing import Callable

from boilerplate_python.domain.interfaces.user_service_interface import IUserService

user_service_global: IUserService = None


def set_use_cases(
        user_service: IUserService
        ):

    global user_service_global
    user_service_global = user_service


def get_use_cases(_type: str) -> Callable:

    return {
        "user_service": lambda: user_service_global
    }.get(_type)
