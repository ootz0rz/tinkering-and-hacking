# https://leetcode.com/problems/word-search/

from typing import List, Optional

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
VISITED = "-"


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0 or len(word) == 0:
            return False

        lenx = len(board)
        leny = len(board[0])

        def start_search_at(x: int, y: int, remainder: str):
            nonlocal board, word

            if len(remainder) == 0:
                return True

            if x < 0 or x >= lenx or y < 0 or y >= leny:
                return False

            if board[x][y] != remainder[0]:
                return False

            # continue searching neighbours
            res = False
            board[x][y] = VISITED
            for xdir, ydir in DIRS:
                nx = x + xdir
                ny = y + ydir

                res = start_search_at(nx, ny, remainder[1:])

                if res:
                    # done
                    break

            # cleanup/backtrack
            board[x][y] = remainder[0]

            return res

        # search for our first letter first
        for ix, row in enumerate(board):
            for iy, cell in enumerate(board[ix]):
                if start_search_at(ix, iy, word):
                    return True

        return False


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sfunc = s.exist

    check_solution_simple(
        sfunc,
        args=[
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "Z",
        ],
        expected=False,
    )

    check_solution_simple(
        sfunc,
        args=[
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "A",
        ],
        expected=True,
    )

    check_solution_simple(
        sfunc,
        args=[
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
        ],
        expected=True,
    )

    check_solution_simple(
        sfunc,
        args=[
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
        ],
        expected=True,
    )

    check_solution_simple(
        sfunc,
        args=[
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
        ],
        expected=False,
    )

    check_solution_simple(
        sfunc,
        args=[
            [["A", "A"]],
            "AAA",
        ],
        expected=False,
    )

    check_solution_simple(
        sfunc,
        args=[
            [["A", "A"]],
            "AAA",
        ],
        expected=False,
    )
