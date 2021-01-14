def longest_palindromic_substring(string):
    ans = ""
    for i in range(len(string)):
        even = helper(string, i, i+1)
        odd = helper(string, i, i)
        ans = max(ans, even, odd, key=len)

    return ans


def helper(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            break

    return string[left+1:right]


print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))
