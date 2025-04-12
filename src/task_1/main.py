# import os
# import sys
from pathlib import Path

# Add 'src' directory to the Python path to use it as a root (not PEP-compliant)
# modules_root_dir = os.path.abspath(Path(__file__).parent.parent)
# sys.path.insert(1, modules_root_dir)
# sys.path.append("../..") # optional simpler relative way

from salary_calculator import total_salary
from utils.logging_handler import init_logging
from utils.error_handler import report_content_errors

DATA_FILE_REL_PATH = "dataset/salary_file.txt"
LOG_FILE_REL_PATH = "task_1.log"

current_folder_path = Path(__file__).parent

if __name__ == "__main__":
    # Initialize the environment (e.g., logging)
    init_logging(current_folder_path / LOG_FILE_REL_PATH)

    # Calculate total salary and average salary
    total, average, content_err = total_salary(current_folder_path / DATA_FILE_REL_PATH)

    if content_err:
        # Log any potential issues with content data
        report_content_errors(content_err, LOG_FILE_REL_PATH)

    # Display results
    if total is not None and average is not None:
        print(f"Total salary: {total}, Average salary: {average}")
