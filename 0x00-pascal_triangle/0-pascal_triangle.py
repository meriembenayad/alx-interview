#!/usr/bin/python3

def pascal_triangle(n):
    """
        Returns a list of lists of integers representing the Pascal’s triangle of n
        Args: n
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n <= 0:
        return []

    triangle = [[1]]  # The first row always 1.
    # For each next row up to n...
    for i in range(1, n):
        row = [1]  # Each row starts with 1.
        last_row = triangle[-1]  # Get the last row of the triangle.
        # For each pair of adjacent numbers in the last row...
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j+1])
        row.append(1)  # Each row ends with 1.
        triangle.append(row)  # Add the row to the triangle.
    return triangle  # Return the completed triangle.
