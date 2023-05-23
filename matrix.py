import random
from iterative import iterative
from display import display
import timeit
import numpy as np
from divAndCon import divAndCon, combineMatrices


def generateElements(matrix, n):
    lower_bound = -10
    upper_bound = 10
    for i in range(0, n):
        for j in range(0, n):
            random_int = random.randint(lower_bound, upper_bound)
            matrix[i, j] = random_int

    return matrix


n = 3

matrixA = np.empty((n, n), dtype=int)
matrixA = generateElements(matrixA, n)

matrixB = np.empty((n, n), dtype=int)
matrixB = generateElements(matrixB, n)


print("matrix A")
display(matrixA)
print("matrix B")
display(matrixB)

start_time = timeit.default_timer()
result = iterative(matrixA, matrixB)
end_time = timeit.default_timer()
runtime = end_time - start_time
print("Runtime:", runtime, "seconds")
print("Iterative result")

display(result)


start_time = timeit.default_timer()
result = divAndCon(matrixA, matrixB)
end_time = timeit.default_timer()
runtime = end_time - start_time
print("Runtime:", runtime, "seconds")
print("Divide and conquer result")
display(result)
