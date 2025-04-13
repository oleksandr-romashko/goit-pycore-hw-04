"""
This script processes cat data from a file.

Reads the file with data about the cats, validates each line (expects id, name, age),
prints valid records, and logs all validation errors to log file.
"""

from pathlib import Path

from cats_inventory import get_cats_info
from utils.logging_handler import init_logging, print_and_log
from utils.error_handler import report_content_errors

def main():
    """
    Main entry point of the script.

    This function processes the cat data file, validates the records (expects id, name, and age),
    prints valid records, and logs any validation errors.
    """
    data_file_rel_path = "dataset/cats_file.txt"
    log_file_rel_path = "task_2.log"

    current_folder_path = Path(__file__).parent

    # Initialize the environment (e.g., logging)
    init_logging(current_folder_path / log_file_rel_path)

    try:
        # Retrieve cats data with potential content lines issues
        cats_info, content_err = get_cats_info(current_folder_path / data_file_rel_path)

        # Report potential file content lines issues
        if content_err:
            report_content_errors(content_err, log_file_rel_path)

        if cats_info:
            # Display results
            print(cats_info)
        else:
            # Handle case and warn user when all file lines have issues
            if content_err:
                print_and_log(
                    f'After processing "{data_file_rel_path}" file, no valid data found in the file".',
                    level="WARNING"
                )
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError, ValueError) as exc:
        print_and_log(str(exc), level="ERROR")
    except Exception as exc:
        print_and_log(f"An unexpected error occurred: {exc}", level="ERROR")

if __name__ == "__main__":
    main()
