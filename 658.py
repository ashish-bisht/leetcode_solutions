def find_closest(nums, k, x):
    import heapq

    heap = []

    for num in nums:
        heapq.heappush(heap, (abs(x-num), num))

    res = []

    while k > 0:
        res.append(heapq.heappop(heap)[1])
        k -= 1
    res.sort()
    return res


print(find_closest([1, 2, 3, 4, 5], 4, -1))
print(find_closest([1, 2, 3, 4, 5], 4, 3))
