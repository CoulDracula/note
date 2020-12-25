# -*- coding: utf-8 -*-
"""
function：
[12 -3  3] [x1] = [15]
[18 -3  1] [x2] = [15]
[-1  2  1] [x3] = [ 6]
"""

import sys
import numpy as np


def many_line_elimination(matrix):
    a = matrix
    n = a.shape[0]
    # step 1: to a triangle matrix
    for k in range(0, n - 1):  # 0,1,2,...,n-2
        print(a)
        if np.abs(a[k, k]) < 1e-6:
            print("error")
            sys.exit(1)
        for i in range(k + 1, n):  # k+1, k+2, ..., n-1
            a[i, k] /= a[k, k]
            for j in range(k + 1, n + 1):
                a[i, j] -= a[i, k] * a[k, j]
    return n


def back_to_generation(matrix, transform_result):
    a = matrix
    n = transform_result
    # step 2:
    # a[n-1,n] /= a[n-1][n-1]
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += a[i, j] * a[j, n]
        a[i, n] = (a[i, n] - sum) / a[i, i]
    return a[:, n]


def gaussian_elimination_solver(matrix):
    # step 1:
    transform_result = many_line_elimination(matrix)
    # step 2:
    result = back_to_generation(matrix, transform_result)
    print(result)


initial_matrix = np.array([[12., -3., 3., 15.],
                           [18., -3., 1., 15.],
                           [-1., 2., 1., 6.]])
gaussian_elimination_solver(initial_matrix)
