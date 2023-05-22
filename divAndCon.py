import numpy as np


def divAndCon(matrix_a, matrix_b):
    r1, c1 = matrix_a.shape
    r2, c2 = matrix_b.shape
    if (r1 == 1 and r2 == 1 and c1 == 1 and c2 == 1):
        result = np.empty((1, 1), dtype=int)
        result[0] = matrix_a[0]*matrix_b[0]
        return result


def splitMatrix(matrix):
    r, c = matrix.shape
    r1 = (r//2)
    r2 = r - r1
    c1 = c//2
    c2 = c - c1
    A = np.empty((r1, c1), dtype=int)
    B = np.empty((r1, c2), dtype=int)
    C = np.empty((r2, c1), dtype=int)
    D = np.empty((r2, c2), dtype=int)

    for i in range(r):
        for j in range(c):
            if (i < r1 and j < c1):
                A[i][j] = matrix[i][j]
            elif (i < r1 and j >= c1):
                B[i][j-c1] = matrix[i][j]
            elif (i >= r1 and j < c1):
                C[i-r1][j] = matrix[i][j]
            elif (i >= r1 and j >= c1):
                D[i-r1][j-c1] = matrix[i][j]
    return A, B, C, D
