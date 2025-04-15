"""
This script visualizes the structure of a given directory path using colored terminal output.

It expects a directory path as a command-line argument, validates the path,
and then recursively prints all subdirectories and files with color distinction
(using the colorama library).

Use the --tree flag to switch between simple and structured output.
"""

import sys
from pathlib import Path
from colorama import init, Fore

from dir_visualizer import visualize_dir_structure, build_dir_tree, display_tree

def main():
    """
    Entry point of the script.

    This function parses command-line arguments to get a target directory path 
    and an optional flag to control the output format. It validates the input 
    path and visualizes the directory structure using one of two methods:

    - Default: A simple recursive layout with colorized output.
    - With --tree: A structured representation using nested dictionaries.

    Command-line arguments:
        path (str): Required. Path to the directory to visualize.
        --tree (flag): Optional. Displays the structure using a structured tree view.

    Returns:
        None
    """

    # Initialize colorama for Windows compatibility
    init(autoreset=True)

    # Determine the base path
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            args.append(arg)

    if args:
        path = (Path(__file__).parent / args[0]).resolve()
    else:
        path = Path.cwd()

    # Validate path
    if not path.exists():
        print(Fore.RED + f"Error: The path '{path}' does not exist.")
        sys.exit(1)

    if not path.is_dir():
        print(Fore.RED + f"Error: The path '{path}' is not a directory.")
        sys.exit(1)

     # Visualize
    if "--tree" in sys.argv:
        # Option - More complex architecture-wise solution using
        #          data structure-based tree representation
        dir_tree = build_dir_tree(path)
        display_tree(dir_tree)
    else:
        # Option - More straight-forward approach
        visualize_dir_structure(path)

if __name__ == "__main__":
    main()
