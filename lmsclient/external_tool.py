import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ExternalToolException(Exception):
    """Canvas client exception
    """
    pass


class ExternalTool:
    """Assignment class
    """
    pass