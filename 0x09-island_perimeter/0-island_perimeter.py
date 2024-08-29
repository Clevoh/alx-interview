#!/usr/bin/python3
""" Island perimeter problem
"""


def island_perimeter(grid):
    """ Calculates the perimeter of an island described in grid.
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row_index in range(rows):
        for col_index in range(cols):
            if grid[row_index][col_index] == 1:
                cell_perimeter = 4

                # Check the upper neighbor
                if row_index > 0 and grid[row_index - 1][col_index] == 1:
                    cell_perimeter -= 2

                # Check the left neighbor
                if col_index > 0 and grid[row_index][col_index - 1] == 1:
                    cell_perimeter -= 2

                # Add the calculated perimeter for the current cell
                perimeter += cell_perimeter

    return perimeter
