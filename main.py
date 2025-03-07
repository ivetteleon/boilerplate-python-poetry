
#from boilerplate_python.infrastructure.triggers.cli import Cli
from boilerplate_python.infrastructure.fast_api.executor import FastApi

from boilerplate_python.application.services.user_service import UserService
from boilerplate_python.infrastructure.repository.user_repository_firestore import UserRepositoryFirestore
def handler() -> None:

    # Create the services instances
    user_repository = UserRepositoryFirestore()

    fast_api = FastApi(
        UserService(user_repository),
    )
    
    fast_api.start()

    #cli = Cli(example_get_data_use_case)
    #cli.start()


if __name__ == "__main__":  

    handler()
