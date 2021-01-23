def search(nums, target):
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    rotated_index = get_rotated_index(nums, target, 0, len(nums)-1)

    check_before_pivot = binary_search(nums, 0, rotated_index-1, target)
    check_after_pivot = binary_search(nums, rotated_index, len(nums)-1, target)
    if check_before_pivot > -1:
        return check_before_pivot
    if check_after_pivot > -1:
        return check_after_pivot
    return -1


def get_rotated_index(nums, target, left, right):
    while left < right:
        mid = left + (right-left)//2

        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid

    return left


def binary_search(nums, left, right, target):
    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1

        else:
            left = mid+1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([1, 3], 1))
print(search([5, 1, 3], 5))
