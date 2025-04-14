"""
Module for visualizing and building directory structures.

This module provides functionality to recursively display the structure of a directory, 
as well as to build and display it in a hierarchical format. It supports sorting of 
files and directories alphabetically, and colorizes the output for better readability.
"""

from pathlib import Path
from typing import Optional, Dict

from colorama import Fore

INDENT_PER_LEVEL = " " * 4

DirectoryTree = Dict[str, Optional["DirectoryTree"]]

def visualize_dir_structure(path: Path, depth: int =0):
    """
    Recursively prints the structure of a directory using indentation and colorized output.

    Files and directories are sorted alphabetically (ascending) by name.
    The function uses blue color for directories and green for files.

    Args:
        path (Path): The directory path to visualize.
        depth (int, optional): The current depth level in the directory tree. 
                               Used internally for recursive indentation.

    Returns:
        None
    """
    if depth == 0:
        print(Fore.BLUE + f"{path.name}/")

    sorted_dir_files = sorted(path.iterdir(), key=lambda x: x.name.lower())

    for entry in sorted_dir_files:
        indentation = INDENT_PER_LEVEL * (depth + 1)
        if entry.is_dir():
            # Print directory and recurse into subdirectory
            print(f"{indentation}{Fore.BLUE}{entry.name}/")
            visualize_dir_structure(entry, depth + 1)
        else:
            # Print file
            print(f"{indentation}{Fore.GREEN}{entry.name}")

def build_dir_tree(path: Path) -> DirectoryTree:
    """
    Recursively builds a directory tree starting from the given path,
    including the root element as the top-level key.

    Args:
        path (Path): The directory path to start building the tree from.

    Returns:
        DirectoryTree: A nested dictionary representing the directory tree.
    """
    def _build(current_path: Path) -> DirectoryTree:
        tree: DirectoryTree = {}
        sorted_dir_files = sorted(current_path.iterdir(), key=lambda x: x.name.lower())
        for entry in sorted_dir_files:
            if entry.is_dir():
                tree[entry.name] = _build(entry)
            else:
                tree[entry.name] = None
        return tree

    # Wrap the result to include the root
    return {path.name: _build(path)}

def display_tree(tree: DirectoryTree, level: int = 0):
    """
    Recursively prints a structured directory tree from a nested dictionary.

    This function takes a pre-built directory tree (created using `build_dir_tree`)
    and displays its hierarchical structure using indentation and color coding.

    - Directories are printed in blue followed by a slash.
    - Files are printed in green.

    Args:
        tree (DirectoryTree): A nested dictionary representing the directory tree.
        level (int, optional): The current depth level for indentation (used internally).

    Returns:
        None
    """
    for name, subtree in tree.items():
        indent = INDENT_PER_LEVEL * level
        if subtree is None:
            print(f"{indent}{Fore.GREEN}{name}")
        else:
            print(f"{indent}{Fore.BLUE}{name}/")
            display_tree(subtree, level + 1)
