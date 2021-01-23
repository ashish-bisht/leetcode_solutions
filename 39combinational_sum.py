def combinational_sum(nums, target):
    res = []
    helper(nums, target, [], res)
    return res


def helper(nums, target, cur, res):
    if target == 0:
        res.append(cur)
        return

    if target < 0:
        return

    for i in range(len(nums)):
        helper(nums[i:], target - nums[i], cur + [nums[i]], res)


print(combinational_sum([2, 3, 6, 7], 7))
print(combinational_sum([2, 3, 5], 8))
