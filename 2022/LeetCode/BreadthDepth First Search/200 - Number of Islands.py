# https://leetcode.com/problems/number-of-islands/

from typing import List


FILLED = "1"
EMPTY = "0"


def val_at(x, y, grid):
    if is_valid(x, y, grid):
        return grid[x][y]

    return EMPTY


def is_valid(x, y, grid):
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])


def is_visited(x, y, grid):
    return val_at(x, y, grid) == EMPTY


def explore_island(sx, sy, grid):
    if is_valid(sx, sy, grid) and grid[sx][sy] == FILLED:
        grid[sx][sy] = EMPTY

        explore_island(sx + 1, sy, grid)
        explore_island(sx - 1, sy, grid)
        explore_island(sx, sy + 1, grid)
        explore_island(sx, sy - 1, grid)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        islands = 0

        # search for first filled
        for ix, xrow in enumerate(grid):
            # print(f"x:{ix} row:{xrow}")
            for iy, cell in enumerate(xrow):

                if cell == FILLED:
                    explore_island(ix, iy, grid)
                    islands = islands + 1

        return islands


if __name__ == "__main__":
    s = Solution()

    def checkSolution(grid, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.numIslands(grid)
        assert r == expected, msg.format(expected, r)

    checkSolution(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        expected=1,
    )

    checkSolution(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        expected=3,
    )
