def calculate_total(salaries: list[int]) -> int:
    """
    Calculates the total of the provided salaries.

    Args:
        salaries (list[int]): A list of integer salary values.

    Returns:
        int: The total sum of the salaries.
    
    Example:
        >>> calculate_total([1000, 2000, 3000])
        6000
    """
    return sum(salaries)

def calculate_average(salaries: list[int]) -> int:
    """
    Calculates the average salary from the provided list of salaries.

    Args:
        salaries (list[int]): A list of integer salary values.

    Returns:
        int: The average salary, rounded to the nearest integer.

    Example:
        >>> calculate_average([1000, 2000, 3000])
        2000
    """
    if not salaries:
        return 0
    
    return int(round(calculate_total(salaries) / len(salaries), 0))