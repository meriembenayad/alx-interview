#!/usr/bin/python3
""" 0. Minimum Operations """


def minOperations(n):
    """
    Method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n <= 0:
        return 0

    for ch in range(2, int(n**0.5) + 1):
        if n % ch == 0:
            return ch + minOperations(n//ch)
    return n
