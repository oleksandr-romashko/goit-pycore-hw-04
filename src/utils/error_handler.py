from utils.logging_handler import print_and_log

def report_content_errors(errors: list[tuple[int, str, str]], log_file_path: str = "log"):
    """
    Logs and prints potential file content issues.

    Args:
        errors (list of tuples): Each tuple contains (line index, line text, cause).
        log_file_path (str): Path to the log file for reference.
    """
    if not errors:
        return

    max_line_length = max((len(line) for _, line, _ in errors), default=0)

    message = (
        "There are potentially corrupted data in your dataset file "
        "that may lead to wrong results and should be or may require fix:"
    )
    print_and_log(message, level="WARNING")
    print_and_log(f"Please check '{log_file_path}' file for more details.", level="INFO", log=False)

    for line_idx, line_str, cause in errors:
        log_message = (
            f"Line {(str(line_idx) + ':').ljust(4)} "
            f"{line_str.ljust(max_line_length)} - Cause: {cause if cause else 'Unknown'}"
        )
        print_and_log(log_message, level="INFO", print_to_console=False)
