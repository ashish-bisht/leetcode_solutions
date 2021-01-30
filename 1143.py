import functools


def longest_common_sub_seq(str1, str2):
    return helper(str1, 0, str2, 0)


@functools.lru_cache(maxsize=None)
def helper(str1, index1, str2, index2):
    if index1 >= len(str1):
        return 0

    if index2 >= len(str2):
        return 0

    if str1[index1] == str2[index2]:
        return 1 + helper(str1, index1+1, str2, index2+1)

    return max(helper(str1, index1+1, str2, index2), helper(str1, index1, str2, index2+1))


print(longest_common_sub_seq("abcde", "ace"))


def dp(str1, str2):
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


print(dp("abcde", "ace"))
