def combinational_sum(nums, target):
    nums.sort()
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
        if nums[i] > target:
            continue
        if i > 0 and nums[i] == nums[i-1]:
            continue
        helper(nums[i+1:], target-nums[i], cur + [nums[i]], res)


print(combinational_sum([10, 1, 2, 7, 6, 1, 5], 8))
