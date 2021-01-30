def top_elements(nums, k):
    import heapq

    from collections import Counter

    count = Counter(nums)
    heap = []
    for key, val in count.items():
        heapq.heappush(heap, (-val, key))

    res = []

    while k > 0:
        res.append(heapq.heappop(heap)[1])
        k -= 1

    return res


print(top_elements([1, 1, 1, 2, 2, 3], 2))
