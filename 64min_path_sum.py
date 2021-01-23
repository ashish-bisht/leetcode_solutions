
def min_path_sum(matrix):
    row_length = len(matrix)
    col_length = len(matrix[0])

    dp = [[0 for _ in range(col_length)] for _ in range(row_length)]

    # fill first row and col..
    dp[0][0] = matrix[0][0]

    for row in range(1, row_length):
        dp[row][0] = matrix[row][0] + dp[row-1][0]

    for col in range(1, col_length):
        dp[0][col] = matrix[0][col] + dp[0][col-1]

    for row in range(1, row_length):
        for col in range(1, col_length):
            dp[row][col] = min(dp[row-1][col], dp[row]
                               [col-1]) + matrix[row][col]

    return dp[-1][-1]


print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(min_path_sum([[1, 2, 3], [4, 5, 6]]))
