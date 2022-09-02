import logging


def get_logger(module_name: str) -> logging.Logger:
    return logging.getLogger(get_logger_name(module_name))


def get_logger_name(module_name: str) -> str:
    return f'backend.{module_name}'
