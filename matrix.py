import random
from iterative import iterative
from display import display
import timeit

def generateElements(matrix):
    lower_bound = -10
    upper_bound = 10
    n =3
    for i in range(0,n):
        row = []
        for j in range(0,n):
            random_int = random.randint(lower_bound, upper_bound)
            row.append(random_int)
        matrix.append(row)
    return matrix


matrixA = []
matrixA = generateElements(matrixA)

matrixB = []
matrixB = generateElements(matrixB)


# display(matrixA)
# display(matrixB)

start_time = timeit.default_timer()
result = iterative(matrixA,matrixB)
end_time = timeit.default_timer()
runtime = end_time - start_time
print("Runtime:", runtime, "seconds")

# display(result)