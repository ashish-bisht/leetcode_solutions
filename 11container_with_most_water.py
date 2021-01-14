def most_water(nums):
    ans = 0

    left, right = 0, len(nums)-1

    while left < right:
        cur = min(nums[left], nums[right]) * (right - left)
        ans = max(ans, cur)

        if nums[left] > nums[right]:
            right -= 1

        else:
            left += 1

    return ans


print(most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(most_water([1, 1]))
print(most_water([4, 3, 2, 1, 4]))
print(most_water([1, 2, 1]))
