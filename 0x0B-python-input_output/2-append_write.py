#!/usr/bin/python3
"""Intro to I/O Ops in Python."""


def append_write(filename="", text=""):
    """Append data to a file.

    Args:
        filename ('obj':'file':'UTF-8'): File
        text (str): Data

    Returns:
        The appended file and number of characters added.

    """
    with open(filename, 'a', encoding='UTF-8') as myFile:
        return myFile.write(text)
