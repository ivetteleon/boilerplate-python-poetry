"""Main module to exposed FastAPI APP."""
import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from boilerplate_python.application.settings import get_settings

from boilerplate_python.domain.exceptions import OperationException
from boilerplate_python.domain.exceptions import RepositoryException
from boilerplate_python.domain.exceptions import ServiceException

from boilerplate_python.infrastructure.fast_api.routers.example_router import router as example_router
from boilerplate_python.infrastructure.fast_api.dependencies import set_use_cases

from boilerplate_python.domain.interfaces.user_service_interface import IUserService

class FastApi():
    __slots__ = ("logger", "example_get_data_use_ase", "app")

    def __init__(self, user_service: IUserService):

        self.logger = get_settings().general.logger()

        set_use_cases(user_service)

        self.app = FastAPI()
        self.app.include_router(example_router, prefix="/v1", tags=["example_router"])


        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=get_settings().general.cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


        @self.app.exception_handler(ServiceException)
        async def service_exception_handler(_: Request, exc: ServiceException):
            return JSONResponse(
                status_code=exc.code,
                content={"message": exc.message},
            )


        @self.app.exception_handler(OperationException)
        async def operation_exception_handler(_: Request, exc: OperationException):
            return JSONResponse(
                status_code=exc.code,
                content={"message": exc.message},
            )


        @self.app.exception_handler(RepositoryException)
        async def repository_exception_handler(_: Request, exc: RepositoryException):
            return JSONResponse(
                status_code=exc.code,
                content={"message": exc.message},
            )


        @self.app.middleware("http")
        def set_trace_log(request: Request, call_next):
            if trace_header := request.headers.get("X-Cloud-Trace-Context"):
                settings = get_settings()
                trace = trace_header.split("/")
                self.logger.set_context(
                    {
                        "logging.googleapis.com/trace": f"projects/{settings.general.gcp_project_id}/traces/{trace[0]}"
                    }
                )
            
            response = call_next(request)
            return response


        @self.app.get("/healthz", include_in_schema=False)
        def healthcheck() -> dict[str, str]:
            """Health Check endpoint."""
            self.logger.get_context().info("STATUS -> OK")
            return {"status": "ok"}

    
    def start(self) -> None:

        uvicorn.run(self.app, host="0.0.0.0", port=8080)

