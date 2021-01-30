import heapq
from collections import Counter


def frequency_sort(string):
    heap = []

    count = Counter(string)

    for key, val in count.items():
        heapq.heappush(heap, (-val, key))
    res = ""
    while heap:
        val, key = heapq.heappop(heap)
        res = res + (-val)*key

    return res


print(frequency_sort("Aabb"))
