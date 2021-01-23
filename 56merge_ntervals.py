def merge_intervals(intervals):
    if not intervals:
        return []
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


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge_intervals([[1, 4], [4, 5]]))
