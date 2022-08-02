# https://leetcode.com/problems/house-robber-ii/

from typing import List, Optional, Dict


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        N = len(nums)

        memo[N - 1] = True
        i = N - 2
        while i >= 0:
            max_jump = min(i + nums[i], N - 1)
            j = i + 1
            while j <= max_jump:
                if j in memo and memo[j]:
                    memo[i] = True
                    break
                j = j + 1

            i = i - 1

        return 0 in memo and memo[0]


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.canJump
    check_solution_simple(
        sf,
        args=[[2, 3, 1, 1, 4]],
        expected=True,
    )

    check_solution_simple(
        sf,
        args=[[3, 2, 1, 0, 4]],
        expected=False,
    )
