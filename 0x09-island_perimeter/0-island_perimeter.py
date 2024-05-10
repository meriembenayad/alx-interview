#!/usr/bin/python3
""" 0. Island Perimeter """


def island_perimeter(grid):
    """
        Calculate the perimeter of the island
        Arg:
            - grid: list of list of integers
        Return:
            - perimeter of island or nothing
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if cell is a land (1)
            if grid[i][j] == 1:
                perimeter += 4
                # Check each side of the cell
                if i > 0 or grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 or grid[i][j - 1] == 0:
                    perimeter -= 2

    return perimeter
