def min_in_sorted(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = left + (right-left)//2

        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid

    return nums[left]


print(min_in_sorted([3, 4, 5, 1, 2]))
print(min_in_sorted([3, 4, 5, 0, 1, 2]))
print(min_in_sorted([3, 1, 2]))
