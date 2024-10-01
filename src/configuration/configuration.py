import logging
from logging.config import dictConfig

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel, BaseSettings


class Config(BaseSettings):
    """
    Variables contained in this model will attempt to load from .env or environment and if variable is missing,
    it will throw exception.
    """

    LOG_LEVEL: str = "INFO"
    BASE_URL: str
    DASHBOARD_URL: str

    class Config:
        env_file = find_dotenv(".env", raise_error_if_not_found=True)


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "report-portal-test"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "INFO"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }


load_dotenv(find_dotenv(".env", raise_error_if_not_found=True))
config = Config()

# Setup logger
dictConfig(LogConfig(LOG_LEVEL=config.LOG_LEVEL).dict())
logger = logging.getLogger("report-portal-test")
