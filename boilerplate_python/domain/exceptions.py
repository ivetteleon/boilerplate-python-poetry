class ServiceException(Exception):
    __slots__ = ("code", "message")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


class OperationException(Exception):
    __slots__ = ("code", "message")

    def __init__(self, code: int, message: str, function: str, obj: str):
        self.code = code
        self.message = f"{function.upper()}:{obj.upper()} | {message}"


class RepositoryException(Exception):
    __slots__ = ("code", "message")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
