#!/usr/bin/python3
""" 0.Change comes from within """


def makeChange(coins: list, total: int) -> int:
    """
        Determine the fewest number of coins needed to meet a given amount total
        Args:
            - coins (list): list of value of the coins
            - total (int): amount of the coins use
        Return fewest number of coins needed to meet total:
            - if total <= 0: return 0
            - If total != number of coins you have: return -1 
    """
    if total <= 0:
        return 0
    
    if total <= min(coins):
        return -1
    
    dp =  [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1
