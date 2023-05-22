def display(matrix):
    n = len(matrix)

    for i in range(0,n):
        for j in range(0,n):
            print(matrix[i][j],end=' ' )
        print()