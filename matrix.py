import random
from iterative import iterative
from display import display
import timeit
import numpy as np
from divAndCon import divAndCon, combineMatrices
from strassen import strassen
import csv


def generateElements(matrix, n):
    lower_bound = -10
    upper_bound = 10
    for i in range(0, n):
        for j in range(0, n):
            random_int = random.randint(lower_bound, upper_bound)
            matrix[i, j] = random_int

    return matrix


data = [
    ['n', 'iterativeTime', 'divConTime', 'strassenTime']
]

i = 1
r=0
while i < 1200:
    # if ~(i&(i-1))!=0:
    if r==0:
        i = i*2
        r=r+1
        n = i
    elif r==1:
        r=r+1
        n = i+random.randint(0,i-1)
    else:
        r = 0
        n = i + random.randint(0,i-1)



    for repeat in range(2):

        row = []
        # n = 4
        row.append(n)

        matrixA = np.empty((n, n), dtype=int)
        matrixA = generateElements(matrixA, n)

        matrixB = np.empty((n, n), dtype=int)
        matrixB = generateElements(matrixB, n)

        # print("matrix A")
        # display(matrixA)
        # print("matrix B")
        # display(matrixB)

        start_time = timeit.default_timer()
        result = iterative(matrixA, matrixB)
        end_time = timeit.default_timer()
        runtime = end_time - start_time
        # print("Runtime:", runtime, "seconds")
        # print("Iterative result")

        # display(result)
        row.append(runtime)

        start_time = timeit.default_timer()
        result = divAndCon(matrixA, matrixB)
        end_time = timeit.default_timer()
        runtime = end_time - start_time
        # print("Runtime:", runtime, "seconds")
        # print("Divide and conquer result")

        # display(result)
        row.append(runtime)

        start_time = timeit.default_timer()
        result = strassen(matrixA, matrixB)
        end_time = timeit.default_timer()
        runtime = end_time - start_time
        # print("Runtime:", runtime, "seconds")
        # print("Strassen result")

        # display(result)
        row.append(runtime)

        data.append(row)

        csv_file = 'data.csv'

        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)

            for row in data:
                writer.writerow(row)
