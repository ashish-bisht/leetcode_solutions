def palindromic_partioning(string):
    res = []
    helper(string, "", res)

    return res


def helper(string, cur, res):
    if not string:
        return
    if cur == cur[::-1]:
        res.append(cur)

    else:
        return

    for i in range(len(string)):
        helper(string[1:], cur + string[i], res)


print(palindromic_partioning("aab"))
