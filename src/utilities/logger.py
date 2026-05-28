from logging import getLogger
from logging.config import dictConfig

from src.settings.config import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
logger = getLogger()
