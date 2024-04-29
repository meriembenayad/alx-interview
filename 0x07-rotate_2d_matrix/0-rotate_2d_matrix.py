#!/usr/bin/python3
""" 0. Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
        Rotate 2D Matrix 90 degree clockwise in-place
        Args:
            - matrix (list): list of n lists,
            each n integers representing the 2D Matrix
        Return:
            - None, Matrix rotated in-place
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
