import re

from utils.file_handler import retrieve_line_data

ID_PATTERN = re.compile(r"^[a-fA-F0-9]{24}$")

def validate_cat_data(cat: list[str], seen_ids: set[str]):
    """
    Validates a single cat data entry.

    Parameters:
        cat (list[str]): A list of three elements representing the cat's ID, name, and age.
        seen_ids (set[str]): A set of already encountered IDs used to detect duplicates.

    Raises:
        ValueError: If any validation check fails (invalid format, duplicate ID, empty fields, or incorrect age).
                    Combines all encountered errors and provides them as error message.
    """
    errors = []
    
    if len(cat) != 3:
        errors.append("Invalid data format or missing/extra data")
    else:
        # Validate ID
        cat_id = cat[0]
        if not cat_id.strip() or not ID_PATTERN.match(cat_id):
            errors.append("Invalid or missing ID")
        elif cat_id in seen_ids:
            errors.append("Duplicate ID")

        # Validate name
        name = cat[1]
        if not name or not name.strip():
            errors.append("Missing or empty name")

        # Validate age
        age_str = cat[2]
        try:
            age = int(age_str)
            if age < 0:
                errors.append("Age cannot be negative")
        except (ValueError, TypeError):
            errors.append("Age must be a numeric integer")

    if errors:
        # Combine all errors into a string and provide it as error message 
        raise ValueError(", ".join(errors))

def get_cats_info(path: str) -> tuple[list[dict[str, str]], list[tuple[int, str, str]]]:
    """
    Retrieves and validates cat data from a file.

    Parameters:
        path (str): Path to the data file.

    Returns:
        Tuple:
        - List of valid cat data dictionaries with keys "id", "name", and "age".
        - List of errors from invalid lines: (line index, line content, error message).
    """
    result = {
        "data": [],
        "seen_ids": set(),
        "line_errors": []
    }

    try:
        # Load file with cat data
        with open(path, encoding="utf-8") as file:
            # Check if file is empty
            if path.stat().st_size == 0:
                raise ValueError(f'The file "{path}" is empty.')

            for line_idx, line in enumerate(file, start=1):
                line = line.rstrip("\n")
                try:
                    # Retrieve cat data from each line
                    cat = retrieve_line_data(line)

                    # Validate cat data
                    validate_cat_data(cat, result["seen_ids"])

                    # Add valid cat data to the list
                    result["data"].append({"id": cat[0], "name": cat[1], "age": cat[2]})
                except ValueError as exc:
                    result["line_errors"].append((line_idx, line, f"{exc}"))
    except FileNotFoundError as exc:
        raise FileNotFoundError(f'The file "{path}" does not exist.') from exc
    except PermissionError as exc:
        raise PermissionError(f'You do not have permission to access "{path}" file.') from exc
    except IsADirectoryError as exc:
        raise IsADirectoryError(f'Expected a file, but found a "{path}" directory.') from exc
    except OSError as exc:
        raise OSError(f"OS error occurred: {exc}") from exc

    return result["data"], result["line_errors"]
