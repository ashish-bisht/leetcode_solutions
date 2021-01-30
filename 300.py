
def longest_increasing_subseq(nums):
    return helper(nums, 0, float("-inf"), {})


def helper(nums, index, last_num, cache):
    if index >= len(nums):
        return 0

    if (index, last_num) in cache:
        return cache[(index, last_num)]
    with_current_index = 0
    if nums[index] > last_num:
        with_current_index = 1 + helper(nums, index+1, nums[index], cache)

    without_current_index = helper(nums, index+1, last_num, cache)

    res = max(with_current_index, without_current_index)

    cache[(index, last_num)] = res

    return res


print(longest_increasing_subseq([10, 9, 2, 5, 3, 7, 101, 18]))


def longest_increasing_subseq_dp(nums):
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


print(longest_increasing_subseq_dp([10, 9, 2, 5, 3, 7, 101, 18]))
