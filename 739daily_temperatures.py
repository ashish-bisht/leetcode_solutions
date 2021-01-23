def daily_temperatures(nums):
    res = [0] * len(nums)

    stack = []

    for i in reversed(range(len(nums))):
        if stack and stack[-1][0] > nums[i]:
            res[i] = stack[-1][1] - i
        elif stack and stack[-1][0] <= nums[i]:
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1][1] - i
        stack.append((nums[i], i))

    return res


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_temperatures([1, 3, 0, 2]))
print(daily_temperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
