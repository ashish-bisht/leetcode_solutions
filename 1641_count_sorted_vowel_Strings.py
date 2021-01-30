

def count_vowels_strings(n):
    res = []
    vowels = "aeiou"
    helper(vowels, n, '', res)
    return res


def helper(vowels, n, cur, res):
    print(cur)
    if len(cur) == n:
        res.append(cur)
        return

    for i in range(len(vowels)):
        helper(vowels[i:], n, cur + vowels[i], res)


print(count_vowels_strings(2))
