
def partition_label_brute(string):
    left, window_start = 0, 0
    window_end = 0
    res = []
    while left < len(string):
        right = len(string)-1
        cur_char = string[left]

        while True:
            if string[right] == cur_char:
                window_end = max(right, window_end)
                break
            right -= 1
        if left == window_end:
            res.append(window_end - window_start+1)
            window_start = left + 1

        left += 1

    return res


def partition_label(string):

    last_postion_dict = {val: index for index, val in enumerate(string)}
    res = []
    right = 0
    left = 0
    for index, val in enumerate(string):
        right = max(right, last_postion_dict[val])
        if index == right:
            res.append(right-left+1)
            left = right + 1

    return res


print(partition_label("ababcbacadefegdehijhklij"))
print(partition_label(""))
