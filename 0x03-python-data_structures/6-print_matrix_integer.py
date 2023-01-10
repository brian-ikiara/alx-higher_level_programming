#!/usr/bin/python3
"""Prints an integer matrix based on length of passed matrix.

    Args:
        matrix. The matrix passed.
    Returns:
        0.
"""


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]), end='')
        print("")
