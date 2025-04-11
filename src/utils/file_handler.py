SEPARATOR = ","

def retrieve_line_data(line: str, separator: str = SEPARATOR) -> list[str]:
    """
    Splits a given line of text into a list of strings based on a separator.

    Args:
        line (str): The line of text to be split.
        separator (str): The delimiter used to split the line (default is a comma).

    Returns:
        list[str]: A list of strings obtained by splitting the input line by the separator.
    
    Example:
        >>> retrieve_line_data("1000,2000,3000")
        ['1000', '2000', '3000']
    """
    return line.strip().split(separator)