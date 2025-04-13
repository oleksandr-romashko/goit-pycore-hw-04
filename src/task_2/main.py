"""
Main script for Task 2 — processing cat data from a file.

Reads the file with data about the cats, validates each line (expects id, name, age),
prints valid records, and logs all validation errors to log file.
"""

from pathlib import Path

from cats_inventory import get_cats_info
from utils.logging_handler import init_logging, print_and_log
from utils.error_handler import report_content_errors

DATA_FILE_REL_PATH = "dataset/cats_file.txt"
LOG_FILE_REL_PATH = "task_2.log"

current_folder_path = Path(__file__).parent

if __name__ == "__main__":
    # Initialize the environment (e.g., logging)
    init_logging(current_folder_path / LOG_FILE_REL_PATH)

    try:
        # Retrieve cats data with potential content lines issues
        cats_info, errors = get_cats_info(current_folder_path / DATA_FILE_REL_PATH)

        # Report potential file content lines issues
        if errors:
            report_content_errors(errors, LOG_FILE_REL_PATH)

        if cats_info:
            # Display results
            print(cats_info)
        else:
            # Handle case and warn user when all file lines have issues
            if errors:
                print_and_log(
                    f'After processing "{DATA_FILE_REL_PATH}" file, no valid data found in the file".',
                    level="WARNING"
                )
    except (FileNotFoundError, ValueError) as exc:
        # Any non-content related errors
        print_and_log(exc, level="ERROR")
