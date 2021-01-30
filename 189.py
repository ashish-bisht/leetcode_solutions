def rotate_array(nums, k):
    return nums[k+1:] + nums[:k+1]


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
