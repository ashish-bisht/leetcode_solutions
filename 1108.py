def defang_ip(string):
    res = []

    for ch in string:
        if ch == ".":
            res.append("[.]")

        else:
            res.append(ch)

    return ("").join(res)


print(defang_ip("1.1.1.1"))
