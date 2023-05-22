import random
from iterative import iterative
from display import display
import timeit
import numpy as np
from divAndCon import splitMatrix


def generateElements(matrix):
    lower_bound = -10

    upper_bound = 10
    n = 3
    for i in range(0, n):
        for j in range(0, n):
            random_int = random.randint(lower_bound, upper_bound)
            matrix[i, j] = random_int

    return matrix


n = 3

matrixA = np.empty((n, n), dtype=int)
matrixA = generateElements(matrixA)

matrixB = np.empty((n, n), dtype=int)
matrixB = generateElements(matrixB)

A, B, C, D = splitMatrix(matrixA)

display(A)
display(B)
display(C)
display(D)

# display(matrixA)
# display(matrixB)

start_time = timeit.default_timer()
result = iterative(matrixA, matrixB)
end_time = timeit.default_timer()
runtime = end_time - start_time
print("Runtime:", runtime, "seconds")

# display(result)
