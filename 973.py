import heapq


def k_closest(points, K):
    heap = []
    for point in points:
        key = (point[0])**2 + point[1]**2
        heapq.heappush(heap, (key, point))
    res = []
    while K > 0:
        res.append(heapq.heappop(heap)[1])
        K -= 1

    return res


print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))
