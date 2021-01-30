def test(nums):
    res1 = []
    helper1(nums, [], res1)
    print(res1, "[i+1:]")
    res2 = []
    helper2(nums, [], res2)
    print(res2, "[1:]")
    res3 = []
    helper3(nums, [], res3)
    print(res3, "[i:]")


def helper1(nums, cur, res):
    res.append(cur)
    if not nums:
        return

    for i in range(len(nums)):
        helper1(nums[i+1:], cur + [nums[i]], res)


def helper2(nums, cur, res):
    res.append(cur)
    if not nums:
        return

    for i in range(len(nums)):
        helper2(nums[1:], cur + [nums[i]], res)


def helper3(nums, cur, res):
    res.append(cur)
    if not nums:
        return

    for i in range(len(nums)):
        helper2(nums[i:], cur + [nums[i]], res)


print(test([1, 2, 3]))
