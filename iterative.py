import numpy as np


def iterative(matrix_a, matrix_b):
    n, c = matrix_a.shape

    result = np.empty((n, n), dtype=int)

    for i in range(n):
        for j in range(n):
            result[i][j] = 0
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result
