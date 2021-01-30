def edit_distance(word1, word2):
    return helper(word1, word2, 0, 0)


def helper(word1, word2, index1, index2):
    if index1 >= len(word1):
        return len(word2)-index2

    if index2 >= len(word2):
        return len(word1) - index1

    if word1[index1] == word2[index2]:
        return helper(word1, word2, index1+1, index2+1)
    insert = 1 + helper(word1, word2, index1, index2+1)
    delete = 1 + helper(word1, word2, index1+1, index2)
    replace = 1 + helper(word1, word2, index1+1, index2+1)

    return min(insert, delete, replace)


print(edit_distance("horse", "ros"))


def edit_distance_dp(word1, word2):
    row_length = len(word1) + 1
    col_length = len(word2) + 1

    matrix = [[0 for _ in range(col_length)] for _ in range(row_length)]

    # base case
    for row in range(row_length):
        matrix[row][0] = row

    for col in range(col_length):
        matrix[0][col] = col

    for row in range(1, row_length):
        for col in range(1, col_length):
            if word1[row-1] == word2[col-1]:

                matrix[row][col] = matrix[row-1][col-1]
            else:
                matrix[row][col] = 1 + \
                    min(matrix[row-1][col], matrix[row]
                        [col-1], matrix[row-1][col-1])

    return matrix[-1][-1]


print(edit_distance_dp("horse", "ros"))
