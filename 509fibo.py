def fibo(n):
    dp = [0] * (n+1)

    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


print(fibo(4))
print(fibo(2))
print(fibo(3))


def fibo_recursive(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo_recursive(n-1) + fibo_recursive(n-2)


print(fibo_recursive(4))
print(fibo_recursive(2))
print(fibo_recursive(3))
