#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        matrix_row = []
        for j in matrix[i]:
            matrix_row.append(j**2)
        new_matrix.append(matrix_row)
    return new_matrix
