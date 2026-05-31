#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Function returns a list of lists of integers
    representing the Pascal's triangle of n
    """
    pascal = []
    if n <= 0:
        return pascal
    else:
        pascal = [[1]]
        for i in range(n-1):
            new = [1]
            for j in range(len(pascal[i]) - 1):
                new.append(pascal[i][j] + pascal[i][j+1])
            new.append(1)
            pascal.append(new)
        return pascal
