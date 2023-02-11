"""
Author: Leon Burghardt
Created on: 2023-02-11

This module contains functions for printing to the console in different colors.

"""

def print_success(text: str) -> None:
    """
    This function takes a string as input and prints it to the console in green color (success).

    Args:
        text (str): The text to be printed to the console.
    """
    print(f"\033[32m{text}\033[0m")

def print_warning(text: str) -> None:
    """
    This function takes a string as input and prints it to the console in yellow color (warning).

    Args:
        text (str): The text to be printed to the console.
    """
    print(f"\033[33m{text}\033[0m")

def print_error(text: str) -> None:
    """
    This function takes a string as input and prints it to the console in red color (error).

    Args:
        text (str): The text to be printed to the console.
    """
    print(f"\033[31m{text}\033[0m")

