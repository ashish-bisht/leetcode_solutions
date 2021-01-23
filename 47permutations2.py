def permutations(nums):
    nums.sort()
    res = []
    helper(nums, [], res)
    return res


def helper(nums, cur, res):
    if not nums:
        res.append(cur)
        return

    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        helper(nums[:i] + nums[i+1:], cur + [nums[i]], res)


print(permutations([1, 1, 2]))
