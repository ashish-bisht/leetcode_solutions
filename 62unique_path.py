def unique_paths(m, n):
    matrix = [[1 for _ in range(n)] for _ in range(m)]

    for row in range(1, m):
        for col in range(1, n):
            matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]

    return matrix[-1][-1]


print(unique_paths(3, 7))
