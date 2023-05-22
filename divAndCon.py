import numpy as np


def divAndCon(matrixA, matrixB):
    r1, c1 = matrixA.shape
    r2, c2 = matrixB.shape
    if (r1 == 1 and r2 == 1 and c1 == 1 and c2 == 1):
        result = np.empty((1, 1), dtype=int)
        result[0] = matrixA[0]*matrixB[0]
        return result
    A11, A12, A21, A22 = splitMatrix(matrixA)
    B11, B12, B21, B22 = splitMatrix(matrixB)

    P1 = divAndCon(A11, B11)
    P2 = divAndCon(A12, B21)
    P3 = divAndCon(A11, B12)
    P4 = divAndCon(A12, B22)
    P5 = divAndCon(A21, B11)
    P6 = divAndCon(A22, B21)
    P7 = divAndCon(A21, B12)

    C11 = addMatrices(P1, P2)
    C12 = addMatrices(P3, P4)
    C21 = addMatrices(P5, P6)
    C22 = addMatrices(addMatrices(P7, P1), addMatrices(-P3, P5))

    Result = combineMatrices(C11, C12, C21, C22)

    return Result


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
