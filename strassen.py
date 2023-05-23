import numpy as np
from display import display
from matrixFunc import splitMatrix, combineMatrices, addMatrices


def strassen(matrixA, matrixB):
    n, _ = matrixA.shape
    newN = 2 ** (int(np.ceil(np.log2(n))))
    A = np.empty((newN, newN), dtype=int)
    B = np.empty((newN, newN), dtype=int)
    A = np.zeros((newN, newN))
    B = np.zeros((newN, newN))
    A = A.astype(int)
    B = B.astype(int)
    A[:n, :n] = matrixA
    B[:n, :n] = matrixB
    resultPadded = strassensAlgo(A, B)
    result = resultPadded[:n, :n]
    return result


def strassensAlgo(matrixA, matrixB):
    n, _ = matrixA.shape

    if (n == 1):
        result = np.empty((1, 1), dtype=int)
        result[0] = matrixA[0]*matrixB[0]
        return result
    A11, A12, A21, A22 = splitMatrix(matrixA)
    B11, B12, B21, B22 = splitMatrix(matrixB)

    P1 = strassensAlgo(A11, addMatrices(B12, -B22))
    P2 = strassensAlgo(addMatrices(A11, A12), B22)
    P3 = strassensAlgo(addMatrices(A21, A22), B11)
    P4 = strassensAlgo(A22, addMatrices(B21, -B11))
    P5 = strassensAlgo(addMatrices(A11, A22), addMatrices(B11, B22))
    P6 = strassensAlgo(addMatrices(A12, -A22), addMatrices(B21, B22))
    P7 = strassensAlgo(addMatrices(A11, -A21), addMatrices(B11, B12))

    C11 = addMatrices(addMatrices(P5, P4), addMatrices(-P2, P6))
    C12 = addMatrices(P1, P2)
    C21 = addMatrices(P3, P4)
    C22 = addMatrices(addMatrices(P1, P5), addMatrices(-P3, -P7))

    Result = combineMatrices(C11, C12, C21, C22)

    return Result
