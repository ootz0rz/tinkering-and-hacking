# https://leetcode.com/problems/climbing-stairs/

from typing import List, Optional, Dict


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def _climb(i, n):
            nonlocal memo

            if i > n:
                return 0

            if i == n:
                return 1

            if i in memo:
                return memo[i]

            memo[i] = _climb(i + 1, n) + _climb(i + 2, n)

            return memo[i]

        return _climb(0, n)


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.climbStairs
    check_solution_simple(
        sf,
        args=[2],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=[3],
        expected=3,
    )
