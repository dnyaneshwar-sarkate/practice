## Python programme to find the transpose of a matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [[j[i] for j in matrix] for i in range(len(matrix[0]))]
print(transpose)