from .logger import logger


def error_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exc:
            logger.error(f"{func.__name__} encountered an uncaught exception - {exc}")

    return inner_function
