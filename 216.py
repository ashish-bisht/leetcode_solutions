def combinational_sum(count, total):
    res = []
    nums = [i for i in range(1, 10)]
    dfs(nums, total, count, [], res)
    return res


def dfs(nums, total, count, cur, res):
    if count == len(cur) and sum(cur) == total:
        res.append(cur)

    for i in range(len(nums)):
        dfs(nums[i+1:], total, count, cur + [nums[i]], res)


print(combinational_sum(3, 7))
