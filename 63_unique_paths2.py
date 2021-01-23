def unique_paths(matrix):
    row_length = len(matrix)
    col_length = len(matrix[0])
    dp = [[0 for _ in range(col_length)] for _ in range(row_length)]

    for row in range(row_length):
        if matrix[row][0] == 1:
            break
        dp[row][0] = 1

    for col in range(col_length):
        if matrix[0][col] == 1:
            break
        dp[0][col] = 1

    for row in range(1, row_length):
        for col in range(1, col_length):
            if matrix[row][col] == 1:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

    return dp[-1][-1]


print(unique_paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(unique_paths([[0, 1], [0, 0]]))
