import pytest
from boilerplate_python.infrastructure.logger.loguru_logger import Logger

def test_singleton_logger():

    # Crea una instancia de Logger
    logger_instance = Logger()  # Crea una instancia de la clase Logger

    logger_instance_copy = Logger()

    logger_instance.set_context(
            {
                "logging.googleapis.com/trace": f"projects/PROJECT_ID/traces/TRACE[0]"
            }
        )

    Logger().get_context().info("Start")

    assert logger_instance is logger_instance_copy

if __name__ == "__main__":
    pytest.main()