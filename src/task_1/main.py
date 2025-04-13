"""
This script calculates the total and average salary from a given dataset file.
It also logs any issues found in the content of the dataset.
"""

from pathlib import Path

# import os
# import sys
# Add 'src' directory to the Python path to use it as a root (not PEP-compliant)
# modules_root_dir = os.path.abspath(Path(__file__).parent.parent)
# sys.path.insert(1, modules_root_dir)
# sys.path.append("../..") # optional simpler relative way

from salary_calculator import total_salary
from utils.logging_handler import init_logging, print_and_log
from utils.error_handler import report_content_errors

DATA_FILE_REL_PATH = "dataset/salary_file.txt"
LOG_FILE_REL_PATH = "task_1.log"

current_folder_path = Path(__file__).parent

if __name__ == "__main__":
    # Initialize the environment (e.g., logging)
    init_logging(current_folder_path / LOG_FILE_REL_PATH)

    try:
        # Retrieve calculated total and average salary data with potential content lines issues
        (total, average), content_err = total_salary(current_folder_path / DATA_FILE_REL_PATH)

        # Report potential file content lines issues
        if content_err:
            report_content_errors(content_err, LOG_FILE_REL_PATH)

        # Display results
        if total == 0 or average == 0:
            print_and_log("The salary data contains invalid or zero values — all or some lines may be invalid.", level="WARNING")
            print(f"Total salary: {total}, Average salary: {average}")
        else:
            print(f"Total salary: {total}, Average salary: {average}")
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError, ValueError) as exc:
        print_and_log(str(exc), level="ERROR")
    except Exception as exc:
        print_and_log(f"An unexpected error occurred: {exc}", level="ERROR")
