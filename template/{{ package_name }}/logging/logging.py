import logging
import sys
from typing import Optional


def setup_logger(
    *, app_name: str, log_level: str, bind_to: Optional[logging.Logger] = None
) -> logging.Logger:
    """
    Set up a logger with the specified application name and log level.

    Parameters
    ----------
    app_name : str
        The name of the application.
    log_level : str
        The logging level as a string (e.g., 'DEBUG', 'INFO', 'WARNING',
        'ERROR', 'CRITICAL').
    bind_to : Optional[logging.Logger], optional
        An existing logger to bind the new logger's handlers to, by
        default None. Typically used for fastapi applications.
        ```python
        from fastapi.logger import logger as fastapi_logger

        setup_logger(app_name="my_app", log_level="info", bind_to=fastapi_logger)
        ```

    Returns
    -------
    logging.Logger
        The configured logger instance.
    """
    logger = logging.getLogger(app_name)
    normalised_log_level = getattr(logging, log_level.upper()) or logging.INFO
    logger.setLevel(normalised_log_level)

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s [%(levelname)8.8s] %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if bind_to:
        bind_to.handlers = logger.handlers
        bind_to.setLevel(log_level)

    return logger
