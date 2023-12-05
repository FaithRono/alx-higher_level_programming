#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's Triangle with n rows.

    Args:
        n (int): Number of rows in the Pascal's Triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.

    If n <= 0, returns an empty list.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle
