from pathlib import Path
import logging

from utils.file_handler import retrieve_line_data
from utils.math import calculate_total, calculate_average

DATA_FILE_PATH = "task_1/salary_file.txt"
LOG_FILE_PATH = "task_1/task_1.log"

current_folder_path = Path(__file__).parent

logging.basicConfig(
    level = logging.INFO,
    datefmt = "%Y-%m-%d %H:%M:%S",
    format = "%(asctime)s %(levelname)s: %(message)s",
    filename = current_folder_path / LOG_FILE_PATH,
    filemode = 'w'        # 'w' to overwrite each run, or 'a' to append
)

def log_errors(errors: list[tuple[int, str, str]]):
    """
    Logs potential issues that may cause incorrect calculations.
    :para errors: List of found errors with line index, line text and cause.
    """
    if not errors:
        return None
   
    print(f"[WARNING] There are potentially corrupted data in your '{DATA_FILE_PATH}' file, that may " +
            "lead to wrong calculation results and should be or may require fix.")
    print(f"[INFO] Please check '{LOG_FILE_PATH}' file for more details.")

    logging.warning(
        "There are potentially corrupted data in your '%s' file that may lead to wrong calculation results and should be or may require fix.",
        DATA_FILE_PATH
    )
    for line_idx, line_str, cause in errors:
        logging.info("Line %d: %s - Cause: %s", line_idx, line_str.ljust(20), cause)

def total_salary(path: str) -> tuple[int, int]:
    """
    Reads file and calculates total and average salary from data in the file.
    :param path: Relative path to the text file with salary data.
    :return: The total and average salary data in tuple.
    """
    result = {
        "salaries": [],
        "corrupted_lines": []
    }

    path_to_data_file = current_folder_path / path

    try:
        # Load file with salary data
        with open(path_to_data_file, encoding="utf-8") as file:
            # Check if file is empty
            if path_to_data_file.stat().st_size == 0:
                logging.warning("The file \"%s\" is empty.", DATA_FILE_PATH)
                return None

            for line_idx, line in enumerate(file):
                try:
                    # Retrieve salary data from each line
                    _, salary_str = retrieve_line_data(line)
                    salary = int(salary_str)

                    # Log valid edge cases (still added to the salary list)
                    if salary <= 0:
                        reason = "zero" if salary == 0 else "negative"
                        cause = f"Please check if {reason} salary is a valid salary value"
                        result["corrupted_lines"].append((line_idx, line.rstrip("\n"), f"(Valid) {cause}"))

                    # Add salary to the list of salaries
                    result["salaries"].append(salary)

                except ValueError as err:
                    # Log invalid edge cases (won't be added to the salary list)
                    cause = err
                    if not salary_str or line.find(",") == -1:
                        cause = "Bad format: value is empty or omitted"
                    elif not str.isnumeric(salary_str):
                        cause = "Salary should be an integer number"
                    result["corrupted_lines"].append((line_idx, line.rstrip("\n"), f"(Invalid) {cause}"))

            # Calculate total and average salaries
            total_salary_value = calculate_total(result["salaries"])
            average_salary_value = calculate_average(result["salaries"])

            # Log any potential issues with data
            log_errors(result["corrupted_lines"])

        return (total_salary_value, average_salary_value)
    except FileNotFoundError:
        print(f"[WARNING] The file \"{DATA_FILE_PATH}\" does not exist.")
        logging.warning("The file \"%s\" does not exist.", DATA_FILE_PATH)
    except PermissionError:
        print(f"[WARNING] You do not have permission to access \"{DATA_FILE_PATH}\" file.")
        logging.warning("You do not have permission to access \"%s\" file.", DATA_FILE_PATH)
    except IsADirectoryError:
        print(f"[WARNING] You do not have permission to access \"{DATA_FILE_PATH}\" file.")
        logging.warning("Expected a file, but found a \"%s\" directory.", DATA_FILE_PATH)
    except OSError as err:
        logging.exception("OS error occurred: %s.", err)
    except Exception as err:
        logging.exception("Unexpected error occurred")

if __name__ == "__main__":
    total, average = total_salary(DATA_FILE_PATH)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
