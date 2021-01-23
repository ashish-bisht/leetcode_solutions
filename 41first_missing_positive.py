def first_positive_integer(nums):
    nums.sort()

    ans = 1
    for num in nums:
        if num == ans:
            ans += 1
    return ans


print(first_positive_integer([1, 2, 0]))
print(first_positive_integer([3, 4, -1, 1]))
print(first_positive_integer([7, 8, 9, 11, 12]))
