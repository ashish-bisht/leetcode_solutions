def kth_largest(nums, k):

    import heapq

    heap = []

    for num in nums:
        heapq.heappush(heap, -num)

    while k > 0:
        ans = heapq.heappop(heap)
        k -= 1

    return -ans


print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
