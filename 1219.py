def get_max_gold(grid):
    max_gold = float("-inf")
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            cur_max = dfs(grid, row, col, 0)
            max_gold = max(cur_max, max_gold)
    return max_gold


def dfs(matrix, row, col, cur):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == 0:
        return cur

    temp = matrix[row][col]

    matrix[row][col] = 0  # vistied

    up = dfs(matrix, row-1, col, cur + temp)
    down = dfs(matrix, row+1, col, cur + temp)
    left = dfs(matrix, row, col-1,  cur + temp)
    right = dfs(matrix, row, col+1, cur + temp)
    res = max(up, down, left, right)
    matrix[row][col] = temp

    return res


print(get_max_gold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
print(get_max_gold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
