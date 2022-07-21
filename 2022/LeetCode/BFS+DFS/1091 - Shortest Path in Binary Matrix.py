# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from typing import List, Optional

EMPTY = 0


def set_visited(x, y, v):
    if not x in v:
        v[x] = {}

    if not y in v[x]:
        v[x][y] = True


def did_visit(x, y, v):
    if x in v:
        if y in v[x]:
            return v[x][y]
    return False


def is_valid(x, y, grid):
    return x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0


def add_if_valid(x, y, o, grid):
    if is_valid(x, y, grid) and grid[x][y] == EMPTY:
        o.append((x, y))


def get_adjacent_empty(x, y, grid):
    o = []

    add_if_valid(x - 1, y - 1, o, grid)
    add_if_valid(x + 1, y + 1, o, grid)

    add_if_valid(x - 1, y + 1, o, grid)
    add_if_valid(x + 1, y - 1, o, grid)

    add_if_valid(x - 1, y, o, grid)
    add_if_valid(x + 1, y, o, grid)

    add_if_valid(x, y - 1, o, grid)
    add_if_valid(x, y + 1, o, grid)

    return o


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1

        if grid[0][0] != EMPTY:
            return -1

        goalX = len(grid) - 1
        goalY = len(grid[0]) - 1

        q = [(0, 0, 0)]  # start at top left with empty path
        v = {}

        while len(q) > 0:
            ix, iy, path = q.pop(0)

            # path.append((ix, iy))
            path = path + 1
            set_visited(ix, iy, v)

            if ix == goalX and iy == goalY:
                return path

            adjacent = get_adjacent_empty(ix, iy, grid)
            for itemx, itemy in adjacent:
                if grid[itemx][itemy] == EMPTY and not did_visit(itemx, itemy, v):
                    q.append(
                        (itemx, itemy, path)
                    )  # explore this node onwards with a copy of path

        return -1


if __name__ == "__main__":
    s = Solution()

    def checkSolution(grid, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.shortestPathBinaryMatrix(grid)
        assert r == expected, msg.format(expected, r)

    checkSolution(
        grid=[[0, 1], [1, 0]],
        expected=2,
    )
