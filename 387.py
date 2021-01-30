def first_unique(string):

    count = {}

    for index, ch in enumerate(string):
        if ch in count:
            count[ch] = float("inf")

        else:
            count[ch] = index
    print(count)
    min_val = float("inf")

    for _, val in count.items():

        min_val = min(min_val, val)
    return min_val if min_val != float("inf") else -1


print(first_unique("leetcode"))
print(first_unique("aa"))
