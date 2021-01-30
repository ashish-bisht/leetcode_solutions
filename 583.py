from functools import lru_cache


def min_distance(str1, str2):
    return helper(str1, 0, str2, 0)


@lru_cache
def helper(str1, index1, str2, index2):
    if index1 >= len(str1):
        return len(str2) - index2

    if index2 >= len(str2):
        return len(str1) - index1

    if str1[index1] == str2[index2]:
        return helper(str1, index1+1, str2, index2+1)

    return 1 + min(helper(str1, index1+1, str2, index2), helper(str1, index1, str2, index2+1))


print(min_distance("sea", "eat"))
