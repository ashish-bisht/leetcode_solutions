def decode_strings(string):
    cur_num = 0
    cur_string = ""
    stack = []

    for ch in string:
        if ch == "[":
            stack.append(cur_string)
            stack.append(cur_num)
            cur_string = ""
            cur_num = 0

        elif ch.isnumeric():
            cur_num = cur_num*10 + int(ch)

        elif ch == "]":
            num = stack.pop()
            last_string = stack.pop()
            cur_string = last_string + num * cur_string

        else:
            cur_string += ch
    return cur_string


print(decode_strings("3[a]2[bc]"))
print(decode_strings("3[a2[c]]"))
print(decode_strings("2[abc]3[cd]ef"))
print(decode_strings("abc3[cd]xyz"))
print(decode_strings("100[leetcode]"))
