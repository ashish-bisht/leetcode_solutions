# sliding window

def longest_substring(string):
    seen = {}

    left, right = 0, 0

    max_so_far = 0

    while left < len(string) and right < len(string):
        cur = string[right]

        if cur in seen:
            left = max(left, seen[cur]+1)

        max_so_far = max(max_so_far, right - left + 1)
        seen[cur] = right

        right += 1

    return max_so_far


print(longest_substring("abcabcbb"))
print(longest_substring("pwwkew"))
print(longest_substring(""))
print(longest_substring("bbbbb"))

print(longest_substring("b"))
print(longest_substring(" "))
print(longest_substring("  "))
print(longest_substring("cdd"))
