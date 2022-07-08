#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) != 0:
        res = list(map(lambda x: [x[i] ** 2 for i in range(len(x))], matrix))
    else:
        res = matrix
    return res
