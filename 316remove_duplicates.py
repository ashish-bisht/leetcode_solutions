def remove_duplicates(string):
    stack = []
    lst = list(string)
    lst.sort()

    for ch in lst:
        if stack and stack[-1] == ch:
            continue
        else:
            stack.append(ch)

    return ("").join(stack)


print(remove_duplicates("bcabc"))
print(remove_duplicates("cbacdcbc"))
