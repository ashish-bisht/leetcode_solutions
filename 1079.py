def letter_pile(string):
    res = []
    helper(string, "", len(string), res)
    return res


def helper(string, cur, max_count, res):
    if cur:

        if len(cur) > max_count:
            return

        res.append(cur)

    for i in range(len(string)):
        if i > 0 and string[i-1] == string[i]:
            continue
        helper(string[:i] + string[i+1:], cur + string[i], max_count, res)


print(letter_pile("AAB"))
