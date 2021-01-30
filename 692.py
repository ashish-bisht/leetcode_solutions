def top_k_frequent(words, k):
    import heapq
    from collections import Counter
    count = Counter(words)
    heap = []

    for key, val in count.items():
        heapq.heappush(heap, (-val, key))
    res = []
    while k > 0:
        res.append(heapq.heappop(heap)[1])
        k -= 1

    return res


print(top_k_frequent(["the", "day", "is", "sunny",
                      "the", "the", "the", "sunny", "is", "is"], 4))
