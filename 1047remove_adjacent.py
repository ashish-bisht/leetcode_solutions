def remove_adjacent(string):
    stack = []

    for ch in string:
        if stack and stack[-1] == ch:
            stack.pop()

        else:
            stack.append(ch)
    return ("").join(stack)


print(remove_adjacent("abbaca"))
