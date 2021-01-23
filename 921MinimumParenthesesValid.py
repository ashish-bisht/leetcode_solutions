def valid(string):
    stack = []

    for ch in string:
        if ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(ch)

        else:
            stack.append(ch)

    return len(stack)


print(valid("())"))
print(valid("((("))
print(valid("()"))
print(valid("()))(("))
