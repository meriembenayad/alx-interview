#!/usr/bin/python3


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
                # Check each side of the cell
                # check above
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # check under
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # check right
                if j == len(grid[0]) or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
