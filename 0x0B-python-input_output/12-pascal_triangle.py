#!/usr/bin/python3
"""Prints Pascal's triangle.

So...it won't be an exact copy of the example shown below,
but we'll be using lists. Yeah :( ... XD

Example:
                    1
                1       1
            1       2       1
        1       3       3       1
    1       4       6       4       1

"""


def pascal_triangle(n):
    """Make a Pascal's triangle row.

    Args:
        n (int): Number

    Returns:
        A row of the Pascal's triangle.

    """
    sumPascal = 0
    rowPascal = []
    if n <= 0:
        return rowPascal
    else:
        for i in range(n):
            for j in range(1, n):
                sumPascal += (i + j)
            rowPascal.append(sumPascal)
        return rowPascal

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
