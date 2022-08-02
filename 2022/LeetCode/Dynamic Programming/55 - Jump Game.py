# https://leetcode.com/problems/house-robber-ii/

from typing import List, Optional, Dict


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums) - 1
        i = N - 1
        while i >= 0:
            if nums[i] + i >= N:
                N = i
            i = i - 1

        return N == 0


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
