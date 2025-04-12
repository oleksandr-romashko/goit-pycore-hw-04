from utils.file_handler import retrieve_line_data
from utils.math_operations import calculate_total, calculate_average
from utils.error_handler import print_and_log

def total_salary(path: str) -> tuple[int | None, int | None, list[tuple[int, str, str]]]:
    """
    Reads file and calculates total and average salary from data in the file.
    :param path: Relative path to the text file with salary data.
    :return: The total and average salary data and content errors (if any) in a tuple.
    """
    result = {
        "salaries": [],
        "line_errors": []
    }

    try:
        # Load file with salary data
        with open(path, encoding="utf-8") as file:
            # Check if file is empty
            if path.stat().st_size == 0:
                print_and_log(f'The file "{path}" is empty.', level="ERROR")
                return (None, None, [])

            for line_idx, line in enumerate(file):
                line = line.rstrip("\n")
                try:
                    # Retrieve salary data from each line
                    _, salary_str = retrieve_line_data(line)
                    salary = int(salary_str)

                    # Add salary to the list of salaries
                    result["salaries"].append(salary)

                    # Log valid edge cases (still will be added to the salary list)
                    if salary <= 0:
                        reason = "zero" if salary == 0 else "negative"
                        cause = f"Please check if {reason} salary is a valid salary value"
                        result["line_errors"].append((line_idx, line, f"(Valid) {cause}"))

                except ValueError as err:
                    # Log invalid edge cases (won't be added to the salary list)
                    cause = err
                    if not line.strip():
                        cause = "Empty line"
                    elif "," not in line:
                        cause = "Line is missing a comma separator"
                    elif not salary_str.isdigit():
                        cause = "Salary should be a numeric integer"
                    else:
                        cause = "Invalid format"

                    result["line_errors"].append((line_idx, line, f"(Invalid) {cause}"))

            # Calculate total and average salaries
            total_salary_value = calculate_total(result["salaries"])
            average_salary_value = calculate_average(result["salaries"])

        return (total_salary_value, average_salary_value, result["line_errors"])
    
    except FileNotFoundError:
        print_and_log(f'The file "{path}" does not exist.', level="ERROR")
    except PermissionError:
        print_and_log(f'You do not have permission to access "{path}" file.', level="ERROR")
    except IsADirectoryError:
        print_and_log(f'Expected a file, but found a "{path}" directory.', level="ERROR")
    except OSError as err:
        print_and_log(f"OS error occurred: {err}", level="ERROR")

    return (None, None, [])
