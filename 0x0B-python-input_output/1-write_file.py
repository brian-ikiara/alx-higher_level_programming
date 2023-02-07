#!/usr/bin/python3
"""Intro to I/O Ops in Python."""


def write_file(filename="", text=""):
    """Write data into a file.

    Args:
        filename ('obj':'file':'UTF-8'): File
        text (str): Data

    Returns:
        A written file.

    """
    with open(filename, 'w', encoding='UTF-8') as myFile:
        return myFile.write(text)
