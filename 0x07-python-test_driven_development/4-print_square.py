#!/usr/bin/python3
"""Program that prints a square."""


def print_square(size):
    """Print a square.

    Args:
        size (int): Square's size.

    Raises:
        TypeError: If !isinstance(size, int)
        ValueError: If size < 0

    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()
    else:
        raise TypeError("size must be an integer")
