# https://leetcode.com/problems/surrounded-regions/

from typing import List, Optional
from collections import deque

CAPTURED = "X"
O = "O"
SAFE = "E"


class Solution:
    def solve(self, board: List[List[str]]) -> List[List[str]]:

        xlen = len(board)
        ylen = len(board[0])

        edge_pieces = [
            [[0], range(ylen)],  # top row
            [[xlen - 1], range(ylen)],  # bottom row
            [range(1, xlen - 1), [0]],  # left column
            [range(1, xlen - 1), [ylen - 1]],  # right column
        ]

        valid_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # -- helpers --

        def get_adjacent(startx, starty):
            for dX, dY in valid_directions:
                x2 = startx + dX
                y2 = starty + dY

                # check bounds
                if not (x2 < xlen and y2 < ylen and x2 >= 0 and y2 >= 0):
                    continue

                if board[x2][y2] != O:
                    continue

                yield (x2, y2)

        def mark_safe(startx, starty):

            if board[startx][starty] != O:
                return

            board[startx][starty] = SAFE

            for nx, ny in get_adjacent(startx, starty):
                mark_safe(nx, ny)

        # -- end helpers --

        # start by searching the borders for any Os, these and their adjacent Os are "safe"
        for xvals, yvals in edge_pieces:
            for x in xvals:
                for y in yvals:
                    if board[x][y] == O:
                        mark_safe(x, y)

        # now traverse the board, any remaining Os are captured, any marked SAFE are reverted to O
        for x, xrow in enumerate(board):
            for y, cell in enumerate(xrow):
                if cell == O:
                    board[x][y] = CAPTURED

                if cell == SAFE:
                    board[x][y] = O

        return board


if __name__ == "__main__":
    s = Solution()

    def checkSolution(
        board, expected, msg="Expected `{0}` at x={1} y={2} but got `{3}`"
    ):
        print("\n\n-----")

        r = s.solve(board)

        for ix, xrow in enumerate(r):
            for iy, cell in enumerate(xrow):
                assert cell == expected[ix][iy], msg.format(
                    expected[ix][iy], ix, iy, cell
                )

        print("Completed test case.")

    checkSolution(
        board=[
            ["X", "X", "X", "X"],
            ["X", "X", "O", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
        ],
        expected=[
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
        ],
    )

    checkSolution(
        board=[
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "O", "X"],
        ],
        expected=[
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "O", "X"],
        ],
    )

    checkSolution(
        board=[
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ],
        expected=[
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ],
    )
