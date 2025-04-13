"""
Reads salary data from a file and calculates the total and average salary.

Each line of the file is expected to contain a name and a numeric salary, separated by a comma.
Lines that are empty, malformed, or contain invalid salary values are logged and ignored in calculations.

Args:
    path (str): Path to the salary data file.

Returns:
    tuple: A tuple where:
        - The first element is another tuple (total_salary, average_salary).
        - The second element is a list of content error tuples: (line_number, line_text, cause).
"""

from utils.file_handler import retrieve_line_data
from utils.math_operations import calculate_total, calculate_average

def explain_salary_line_error(line: str, salary_str: str) -> str:
    """
    Analyzes a salary line to determine the reason for its invalidity and generates an explanation.

    Args:
        line (str): The full line of text from the file containing the salary data.
        salary_str (str): The salary value (as a string) extracted from the line.

    Returns:
        str: A message explaining why the salary line is invalid, including possible causes like missing data,
             incorrect format, or invalid salary values.
    """
    if not line.strip():
        return "Empty line"
    if "," not in line:
        return "Line is missing a comma separator"
    if not salary_str.isdigit():
        return "Salary should be a numeric integer"
    return "Invalid format"

def total_salary(path: str) -> tuple[tuple[int, int], list[tuple[int, str, str]]]:
    """
    Reads salary data from a file, validates and parses it, then calculates total and average salary.

    Each valid line in the file should contain a developer's name and a numeric salary,
    separated by a comma (e.g., "John Doe,3000").

    Invalid lines (e.g., missing salary, incorrect format) are ignored in the calculation and
    returned as part of the content error log.

    Args:
        path (str): Path to the salary data file.

    Returns:
        tuple:
            - A tuple of two integers: (total_salary, average_salary).
            - A list of content error tuples: each tuple contains:
                (line_number, original_line, explanation).
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
                raise ValueError(f'The file "{path}" is empty.')

            for line_idx, line in enumerate(file, start=1):
                line = line.rstrip("\n")
                try:
                    # Retrieve salary data from each line
                    _, salary_str = retrieve_line_data(line)
                    salary = int(salary_str)

                    # Add salary to the list of salaries
                    result["salaries"].append(salary)

                    # Log valid edge cases (item still will be added to the salary list as valid)
                    if salary <= 0:
                        reason = "zero" if salary == 0 else "negative"
                        cause = f"Please check if {reason} salary is a valid salary value"
                        result["line_errors"].append((line_idx, line, f"(Valid) {cause}"))
                except ValueError:
                    # Judge and log invalid edge cases (item won't be added to the salary list as invalid)
                    cause = explain_salary_line_error(line, salary_str)
                    result["line_errors"].append((line_idx, line, f"(Invalid) {cause}"))
    
    except FileNotFoundError as exc:
        raise FileNotFoundError(f'The file "{path}" does not exist.') from exc
    except PermissionError as exc:
        raise PermissionError(f'You do not have permission to access "{path}" file.') from exc
    except IsADirectoryError as exc:
        raise IsADirectoryError(f'Expected a file, but found a "{path}" directory.') from exc
    except OSError as exc:
        raise OSError(f"OS error occurred: {exc}") from exc
    
    # Calculate total and average salaries
    total_salary_value = calculate_total(result["salaries"])
    average_salary_value = calculate_average(result["salaries"])

    return (total_salary_value, average_salary_value), result["line_errors"]
