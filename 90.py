def subsets(nums):
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, cur, res):
    res.append(cur)
    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        dfs(nums[i+1:], cur + [nums[i]], res)


print(subsets([1, 2, 2]))
