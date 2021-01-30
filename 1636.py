def frequency_sort(nums):
    from collections import Counter
    import heapq
    count = Counter(nums)
    heap = []

    for key, val in count.items():
        heapq.heappush(heap, (val, -key))

    res = []

    while heap:
        val, key = heapq.heappop(heap)
        for _ in range(val):
            res.append(-key)

    return res


print(frequency_sort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
print(frequency_sort([2, 3, 1, 3, 2]))
