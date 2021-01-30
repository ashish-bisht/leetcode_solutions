def extra_candy(candies, extraCandies):
    candie_max = max(candies)
    res = []
    for candie in candies:
        if candie + extraCandies >= candie_max:
            res.append(True)
        else:
            res.append(False)
    return res


print(extra_candy([2, 3, 5, 1, 3], 3))
