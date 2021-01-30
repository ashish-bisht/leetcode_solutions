def combinations(n, k):
    res = []
    nums = [i for i in range(1, n+1)]
    dfs(nums, k, [], res)
    return res


def dfs(nums, k, cur, res):
    if k == len(cur):
        res.append(cur)
        return

    for i in range(len(nums)):
        dfs(nums[i+1:], k, cur + [nums[i]], res)


print(combinations(4, 2))
