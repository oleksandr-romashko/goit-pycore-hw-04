import logging

def init_logging(path):
    """
    Initializes environment by setting up logging and other configurations.
    """
    logging.basicConfig(
        level = logging.INFO,
        datefmt = "%Y-%m-%d %H:%M:%S",
        format = "%(asctime)s %(levelname)s: %(message)s",
        filename = path,
        filemode = 'w'        # 'w' to overwrite each run, or 'a' to append
    )

def print_and_log(
        message: str,
        level: str = "INFO",
        print_to_console: bool = True,
        log: bool = True
    ) -> None:
    """
    Logs and/or prints a message with the specified log level.

    Args:
        message (str): The message to be logged and/or printed.
        level (str): The log level to use (e.g., "ERROR", "WARNING", "INFO", "DEBUG"). 
                     Defaults to "INFO". If an unknown level is provided, it defaults to DEBUG logging.
        print_to_console (bool): Whether to print the message to the console. Defaults to True.
        log (bool): Whether to log the message using the logging module. Defaults to True.

    Behavior:
        - Logs using the appropriate logging function based on the level.
        - Falls back to DEBUG logging if the level is unrecognized.
        - Does not raise errors for invalid levels.
    """
    level_upper = level.upper()

    if print_to_console:
        print(f"[{level_upper}] {message}")

    if log:
        match level_upper:
            case "ERROR":
                logging.error(message)
            case "WARNING":
                logging.warning(message)
            case "INFO":
                logging.info(message)
            case "DEBUG":
                logging.debug(message)
            case _:
                logging.debug("(Unrecognized log level '%s', defaulted to DEBUG) %s", level, message)
