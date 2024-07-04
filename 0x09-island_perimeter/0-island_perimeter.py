#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list): A list of lists of integers representing the map.
                    0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the four adjacent cells
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1  # Top edge
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1  # Bottom edge
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1  # Left edge
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1  # Right edge

    return perimeter
