def remove_adjacent(string, k):
    stack = []

    for ch in string:
        print(stack)
        if len(stack) >= k and stack[-1] == ch:
            temp = ""
            for _ in range(k):
                if stack[-1] != ch:
                    break
                cur = stack.pop()
                temp += cur
            if len(temp) < k:
                for _ in range(len(temp)):
                    stack.append(ch)

        else:
            stack.append(ch)
    return ("").join(stack)


print(remove_adjacent("abcd", 2))
print(remove_adjacent("deeedbbcccbdaa", 3))
print(remove_adjacent("pbbcggttciiippooaais", 2))
