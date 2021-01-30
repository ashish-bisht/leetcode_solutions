def monotonic_array(nums):

    increasing = True
    decreasing = True

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            increasing = False

        if nums[i] < nums[i+1]:
            decreasing = False

    return increasing or decreasing


print(monotonic_array([1, 2, 2, 3]))
print(monotonic_array([1, 3, 2]))
