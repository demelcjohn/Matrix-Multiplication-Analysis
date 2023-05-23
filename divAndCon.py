import numpy as np
from display import display
from matrixFunc import splitMatrix, combineMatrices, addMatrices


def divAndCon(matrixA, matrixB):
    r1, c1 = matrixA.shape
    r2, c2 = matrixB.shape

    if (r1 == 1 or r2 == 1 or c2 == 1):
        result = np.empty((r1, c2), dtype=int)
        for i in range(r1):
            for j in range(c2):
                result[i][j] = 0
                for k in range(r2):
                    result[i][j] += matrixA[i][k] * matrixB[k][j]
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
    P8 = divAndCon(A22, B22)

    C11 = addMatrices(P1, P2)
    C12 = addMatrices(P3, P4)
    C21 = addMatrices(P5, P6)
    C22 = addMatrices(P7, P8)

    Result = combineMatrices(C11, C12, C21, C22)

    return Result
