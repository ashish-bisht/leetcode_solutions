def word_search(matrix, word):

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == word[0]:

                is_there = helper(matrix, row, col, word)
                if is_there:
                    return True
    return False


def helper(matrix, row, col, word):
    if not word:
        return True
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] != word[0]:
        return False

    temp = matrix[row][col]
    matrix[row][col] = "#"
    up = helper(matrix, row-1, col,  word[1:])
    right = helper(matrix, row, col+1,  word[1:])
    down = helper(matrix, row+1, col,  word[1:])
    left = helper(matrix, row, col-1,  word[1:])

    res = up or right or left or down
    matrix[row][col] = temp
    return res


print(word_search([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))


print(word_search([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
