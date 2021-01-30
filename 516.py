def longest_palindromic_subseq(string):
    return helper(string, 0, len(string)-1)


def helper(string, left, right):
    if left == right:
        return 1

    if left > right:
        return 0

    if string[left] == string[right]:
        return 2 + helper(string, left+1, right-1)

    return max(helper(string, left+1, right), helper(string, left, right - 1))


print(longest_palindromic_subseq("bbbab"))


def dp(str1):
    str2 = str1[::-1]
    row_len = len(str1)+1
    col_len = len(str2)+1

    matrix = [[0 for _ in range(col_len)] for _ in range(row_len)]

    for row in range(1, row_len):
        for col in range(1, col_len):
            if str1[row-1] == str2[col-1]:
                matrix[row][col] = 1 + matrix[row-1][col-1]

            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1])

    return matrix[-1][-1]


print(dp("bbbab"))
