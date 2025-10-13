import logging
from functools import wraps

logger = logging.getLogger("decorator_logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)

file_handler = logging.FileHandler("decorator.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Result {func.__name__} -> {result}")
            return result
        except Exception as e:
            logger.error(f"Exception caught at [{func.__name__}] function: {e}", exc_info=True)
            raise
    return wrapper


@log_call
def add(a, b):
    return a + b

@log_call
def divide(a, b):
    return a / b


if __name__ == "__main__":
    add(5, 7)
    divide(10, 2)
    divide(10, 0)
