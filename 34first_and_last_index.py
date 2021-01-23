def first_and_last_index(nums, target):

    first_index = first_index_helper(nums, target)
    last_index = last_index_helper(nums, target)

    return [first_index, last_index]


def first_index_helper(nums, target):

    left, right = 0, len(nums)-1
    index = -1
    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] == target:
            index = mid
            right = mid-1

        elif nums[mid] > target:
            right = mid-1

        else:
            left = mid+1
    return index


def last_index_helper(nums, target):
    left, right = 0, len(nums)-1
    index = -1
    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] == target:
            index = mid
            left = mid+1

        elif nums[mid] > target:
            right = mid-1

        else:
            left = mid+1
    return index


print(first_and_last_index([5, 7, 7, 8, 8, 10], 8))
print(first_and_last_index([5, 7, 7, 8, 8, 10], 6))
print(first_and_last_index([], 0))
