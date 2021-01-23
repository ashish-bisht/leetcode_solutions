def next_permutations(nums):

    flag = False

    for i in reversed(range(1, len(nums))):
        if nums[i] > nums[i-1]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            flag = True
            break

    return nums if flag else nums[::-1]


print(next_permutations([1, 2, 3]))
print(next_permutations([3, 2, 1]))
print(next_permutations([1, 1, 5]))
print(next_permutations([1, 1, 5, 4]))
