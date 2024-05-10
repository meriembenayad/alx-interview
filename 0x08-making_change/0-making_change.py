#!/usr/bin/python3
""" 0.Change comes from within """


def makeChange(coins: list, total: int) -> int:
    """
        Determine the fewest number of coins needed to meet
        a given amount total
        Args:
            - coins (list): list of value of the coins
            - total (int): amount of the coins use
        Return fewest number of coins needed to meet total:
            - if total <= 0: return 0
            - If total != number of coins you have: return -1
    """
    if total <= 0:
        return 0

    if coins == [] or coins is None:
        return -1

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break

        n = total // coin
        total -= n * coin
        count += n

    return count if total == 0 else -1
