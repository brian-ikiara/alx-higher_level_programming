#!/usr/bin/python3
"""Intro to I/OOps in Python."""


def read_file(filename=""):
    """Read a file.

    Args:
        filename ('obj':'file':'UTF-8'): File

    """
    with open(filename, "r", encoding="UTF-8") as myFile:
        print(myFile.read(), end='')
