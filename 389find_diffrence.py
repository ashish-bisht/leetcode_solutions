
def find_diffrence(str1, str2):
    ans = 0

    for ch in str1 + str2:
        ans ^= ord(ch)
    return chr(ans)


print(find_diffrence("abcd", "abcde"))
print(find_diffrence("", "y"))
print(find_diffrence("a", "aa"))
print(find_diffrence("ae", "aea"))
