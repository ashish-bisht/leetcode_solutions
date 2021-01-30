def third_max(nums):
    import heapq
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
    k = 3
    while heap and k > 0:
        res = heapq.heappop(heap)
        k -= 1

    return -res


print(third_max([3, 2, 1]))
print(third_max([3, 2]))
print(third_max([1, 2]))
