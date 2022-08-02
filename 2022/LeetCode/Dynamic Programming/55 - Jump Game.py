# https://leetcode.com/problems/house-robber-ii/

from typing import List, Optional, Dict


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        N = len(nums)

        def _can_jump_from(idx):
            nonlocal nums, memo, N

            if idx == N - 1:
                return True

            max_jump = min(idx + nums[idx], N - 1)
            i = max_jump
            while i > idx:
                if _can_jump_from(i):
                    return True
                i = i - 1

            return False

        return _can_jump_from(0)


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
