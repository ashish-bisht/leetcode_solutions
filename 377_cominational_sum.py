def combinationa_sum(nums, target):
    res = []
    helper(nums, target, [], res)
    return len(res)


def helper(nums, target, cur, res):
    if target == 0:
        res.append(cur)
        return
    if target < 0:
        return

    for i in range(len(nums)):
        helper(nums, target - nums[i], cur + [nums[i]], res)


print(combinationa_sum([1, 2, 3], 4))
