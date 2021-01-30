def update_matrix(matrix):
    res = matrix

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                res[row][col] = dfs(matrix, row, col)

    return res


def dfs(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == "X":
        return float("inf")

    if matrix[row][col] == 0:
        return 0

    temp = matrix[row][col]
    matrix[row][col] = "X"
    up = 1 + dfs(matrix, row-1, col)
    down = 1 + dfs(matrix, row+1, col)
    left = 1 + dfs(matrix, row, col-1)
    right = 1 + dfs(matrix, row, col+1)

    res = min(up, down, left, right)
    matrix[row][col] = temp
    return res


print(update_matrix([[0, 0, 0],
                     [0, 1, 0],
                     [1, 1, 1]]))
