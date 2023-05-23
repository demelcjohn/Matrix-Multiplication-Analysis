import numpy as np


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


def addMatrices(A, B):
    r, c = A.shape
    C = np.empty((r, c), dtype=int)
    for i in range(r):
        for j in range(c):
            C[i][j] = A[i][j]+B[i][j]
    return C


def combineMatrices(C11, C12, C21, C22):
    r1, c1 = C11.shape
    r2, c2 = C22.shape
    r = r1+r2
    c = c1+c2
    Result = np.empty((r, c), dtype=int)
    for i in range(r):
        for j in range(c):
            if (i < r1 and j < c1):
                Result[i][j] = C11[i][j]
            elif (i < r1 and j >= c1):
                Result[i][j] = C12[i][j-c1]
            elif (i >= r1 and j < c1):
                Result[i][j] = C21[i-r1][j]
            elif (i >= r1 and j >= c1):
                Result[i][j] = C22[i-r1][j-c1]
    return Result
