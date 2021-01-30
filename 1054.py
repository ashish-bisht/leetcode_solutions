def distant_barcodes(nums):
    from collections import Counter
    import heapq

    count = Counter(nums)
    heap = []

    for key, val in count.items():
        heapq.heappush(heap, (-val, key))

    res = []
    while heap:
        val1, key1 = heapq.heappop(heap)
        res.append(key1)
        val1 = -val1-1

        if heap:
            val2, key2 = heapq.heappop(heap)
            res.append(key2)
            val2 = -val2-1

        if val1 > 0:
            heapq.heappush(heap, (-val1, key1))

        if val2 > 0:
            heapq.heappush(heap, (-val2, key2))

    return res


print(distant_barcodes([1, 1, 1, 1, 2, 2, 3, 3]))
