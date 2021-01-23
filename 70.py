def climbing_stairs(n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    return climbing_stairs(n-1) + climbing_stairs(n-2)


print(climbing_stairs(2))
print(climbing_stairs(3))


def climbing_stairs_dp(n):
    if n == 0:
        return 0

    dp = [0] * (n)

    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


print(climbing_stairs_dp(2))
print(climbing_stairs_dp(3))
