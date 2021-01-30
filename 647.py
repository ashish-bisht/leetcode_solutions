def palindromic_substrings(string):
    res = []
    helper(string, "", res)
    return res


def helper(string, cur, res):

    if cur and cur == cur[::-1] and cur not in res:
        res.append(cur)

    for i in range(len(string)):
        helper(string[i+1:], cur + string[i], res)


print(palindromic_substrings("abc"))
print(palindromic_substrings("aaa"))
print(palindromic_substrings("bccb"))
