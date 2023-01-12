#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_mat = [[] for i in range(len(matrix))]

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            sq_mat[x].append(matrix[x][y] ** 2)
    return sq_mat
