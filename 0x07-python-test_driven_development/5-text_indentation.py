#!/usr/bin/python3
"""
text_indentation module:
This module provides a function to indent text after specific punctuation
marks.
"""


def text_indentation(text):
    """
    Indents text after periods, question marks, and colons.
    Prints the indented text

    Args:
        text: The text to be indented.

    Returns:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    print(text.replace('. ', ".\n\n")
              .replace('? ', "?\n\n")
              .replace(': ', ":\n\n")
              .replace('.', ".\n\n")
              .replace('?', "?\n\n")
              .replace(':', ":\n\n"), end="")
