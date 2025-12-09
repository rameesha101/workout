"""Problem 8: Write a function count_change to count the number of ways to change any given amount. Available coins are also passed as argument to the function.

count_change(10, [1, 5])
3
count_change(10, [1, 2])
6
count_change(100, [1, 5, 10, 25, 50])
292 """

def count_change(amount, coins):
    #if amount becomes 0, there is one way to make change (using no coins)
    if amount == 0:
        return 1
    #if amount becomes negative or no coins left, no way to make change

    if amount < 0 or len(coins) == 0:
        return 0
    
    # there are two possibilities, we include the last coin or we don't
    # include the last coin
    include_last = count_change(amount - coins[0], coins)
    # exclude the last coin
    exclude_last = count_change(amount, coins[1:])

    return include_last + exclude_last    # total ways to make change