def two_sum(nums, target):
    d = {}

    for index, val in enumerate(nums):
        if target-val in d:
            return[index, d[target-val]]
        else:
            d[val] = index

    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
