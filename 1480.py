def running_sum(nums):
    res = [nums[0]]
    for num in nums[1:]:
        res.append(res[-1] + num)

    return res


print(running_sum([1, 2, 3, 4]))
