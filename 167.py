def two_sum(nums, target):

    left = 0
    right = len(nums)-1

    while left < right:
        cur = nums[left] + nums[right]
        if cur == target:
            return [left+1, right+1]
        elif cur > target:
            right -= 1
        else:
            left += 1

    return []


print(two_sum([2, 7, 11, 15], 9))
