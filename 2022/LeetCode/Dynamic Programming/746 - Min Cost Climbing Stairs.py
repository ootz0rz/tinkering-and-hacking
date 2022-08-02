# https://leetcode.com/problems/climbing-stairs/

from typing import List, Optional, Dict


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}

        def calc_min(n):
            nonlocal cost
            if n <= 1:  # start at 0 or 1
                return 0

            if n in memo:
                return memo[n]

            memo[n] = min(
                cost[n - 1] + calc_min(n - 1),
                cost[n - 2] + calc_min(n - 2),
            )

            return memo[n]

        return calc_min(len(cost))


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minCostClimbingStairs
    check_solution_simple(
        sf,
        args=[[10, 15, 20]],
        expected=15,
    )

    check_solution_simple(
        sf,
        args=[[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]],
        expected=6,
    )
