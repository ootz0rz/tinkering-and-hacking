# https://leetcode.com/problems/house-robber-ii/

from typing import List, Optional, Dict


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    def _rob(self, nums):
        ln = len(nums)
        memo = {}

        def rob_max(startidx):
            nonlocal ln, memo, nums
            if startidx >= ln:
                return 0

            if startidx in memo:
                return memo[startidx]

            memo[startidx] = max(
                # try the one next to us instead
                rob_max(startidx + 1),
                # take from this one, and skip a house at least
                rob_max(startidx + 2) + nums[startidx],
            )

            return memo[startidx]

        return rob_max(0)


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.rob
    check_solution_simple(
        sf,
        args=[[1, 2, 3, 1]],
        expected=4,
    )

    check_solution_simple(
        sf,
        args=[[2, 7, 9, 3, 1]],
        expected=12,
    )
