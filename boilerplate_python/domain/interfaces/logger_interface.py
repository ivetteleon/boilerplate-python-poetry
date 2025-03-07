from abc import ABCMeta
from abc import abstractmethod

class ILogger(metaclass=ABCMeta):

    @abstractmethod
    def set_context(ctx: dict):
        ...

    @abstractmethod
    def get_context():
        ...

    @abstractmethod
    def info(message: str) -> None:
        ...


    #@abstractmethod 
    #def debug(message: str) -> None:
    #    ...

    @abstractmethod
    def warning(message: str) -> None:
        ...

    @abstractmethod
    def error(message: str) -> None:
        ...
