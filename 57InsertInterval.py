def insert_interval(intervals, new_interval):
    intervals.append(new_interval)

    intervals.sort()

    last_interval = intervals[0]
    res = []
    for cur_interval in intervals[1:]:
        if cur_interval[0] <= last_interval[1]:
            last_interval[1] = max(cur_interval[1], last_interval[1])
        else:
            res.append(last_interval)
            last_interval = cur_interval

    res.append(last_interval)
    return res


print(insert_interval([[1, 3], [6, 9]], [2, 5]))
print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(insert_interval([], [5, 7]))
print(insert_interval([[1, 5]], [2, 3]))
