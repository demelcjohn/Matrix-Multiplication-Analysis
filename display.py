def display(matrix):
    r, c = matrix.shape

    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=' ')
        print()
