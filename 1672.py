def max_waelth(accounts):
    max_wealth = 0

    for account in accounts:
        max_wealth = max(max_wealth, sum(account))

    return max_wealth


print(max_waelth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
