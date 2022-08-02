# https://leetcode.com/problems/word-search/

from typing import List, Optional


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    check_solution_simple(
        s.exist,
        args=[
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
        ],
        expected=True,
    )
