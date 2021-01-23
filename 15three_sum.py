def three_sum(nums):
    nums.sort()

    res = []
    index = 0
    for index in range(len(nums)):
        if index > 0 and nums[index-1] == nums[index]:
            continue  # no duplicates :D
        helper(nums, index+1, -nums[index], res)
    return res


def helper(nums, left, key, res):
    right = len(nums)-1

    while left < right:
        cur = nums[left] + nums[right]
        if cur == key:
            res.append([nums[left], nums[right], -key])

            # now skip dupicates:
            while left < right and nums[left] == nums[left+1]:
                left += 1

            while left < right and nums[right] == nums[right-1]:
                right -= 1

            left += 1
            right -= 1

        elif cur > key:
            right -= 1

        else:
            left += 1


print(three_sum([-1, 0, 1, 2, -1, -4]))
