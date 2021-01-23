def find_duplicate(nums):
    start = slow = fast = 0

    # proceed till get slow and fast as equal

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # now check when start gets equal to slow

    while True:
        slow = nums[slow]
        start = nums[start]

        if slow == start:
            break
    return start


print(find_duplicate([1, 3, 4, 2, 2]))
print(find_duplicate([3, 1, 3, 4, 2]))
print(find_duplicate([1, 1]))
print(find_duplicate([1, 1, 2]))
