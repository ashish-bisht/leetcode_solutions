def edit_distance(word1, word2):
    return helper(word1, word2, 0, 0)


def helper(word1, word2, index1, index2):
    if index1 >= len(word1):
        return len(word2)-index2

    if index2 >= len(word2):
        return len(word1) - index1

    if word1[index1] == word2[index2]:
        return helper(word1, word2, index1+1, index2+1)
    else:
        insert = 1 + helper(word1, word2, index1, index2+1)
        delete = 1 + helper(word1, word2, index1+1, index2)
        replace = 1 + helper(word1, word2, index1+1, index2+1)

    return min(insert, delete, replace)


print(edit_distance("horse", "ros"))
