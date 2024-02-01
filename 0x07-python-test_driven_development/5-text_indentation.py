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
    new_text = ""
    leadingSpace = True
    ender = ""

    for i in range(len(text)):
        if (i == len(text) - 1 and
            (text[i] != '.' and 
             text[i] != ':' and
             text[i] != '?' and
             text[i] != ' ')):
            ender = '\n'
        if text[i] == '\n':
            new_text += text[i]
            leadingSpace = True
            continue
        if text[i] == ' ':
            if i == len(text) - 1:
                break
            elif text[i + 1] == '\n':
                i += 1
                continue
            elif leadingSpace:
                continue
        leadingSpace = False
        if text[i] != ':' and text[i] != '.' and text[i] != '?':
            new_text += text[i]
            continue
        else:
            new_text += text[i] + "\n\n"
            leadingSpace = True
    print(new_text, end=ender)
