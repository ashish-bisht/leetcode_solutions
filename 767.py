def reorganise_string(string):
    import heapq
    from collections import Counter
    temp = list(string)

    count = Counter(temp)
    heap = []
    for key, val in count.items():
        heapq.heappush(heap, (-val, key))
    res = []
    val2 = -1
    while heap:
        val1, key1 = heapq.heappop(heap)
        if res and res[-1] == key1:
            return ""
        res.append(key1)
        val1 = -val1 - 1
        if heap:
            val2, key2 = heapq.heappop(heap)
            res.append(key2)
            val2 = -val2 - 1

        if val1 > 0:
            heapq.heappush(heap, (-val1, key1))

        if val2 > 0:
            heapq.heappush(heap, (-val2, key2))
    return ("").join(res)


print(reorganise_string("aaab"))
print(reorganise_string("aab"))
print(reorganise_string("bbbbbbbb"))
