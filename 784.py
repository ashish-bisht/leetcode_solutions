def letter_permutations(string):
    res = []
    helper(string, 0, "", res)
    return res


def helper(string, index, cur, res):
    if index == len(string):
        res.append(cur)
        return

    if string[index].isalpha():
        helper(string, index+1, cur + string[index].lower(), res)
        helper(string, index+1, cur + string[index].upper(), res)

    else:
        helper(string, index+1, cur + string[index], res)


print(letter_permutations("a1b2"))
