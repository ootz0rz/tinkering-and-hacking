# https://leetcode.com/problems/jump-game-ii/

from typing import List, Optional, Dict


class Solution:
    def jump(self, nums: List[int]) -> bool:
        memo = {}

        N = len(nums)

        memo[N - 1] = 0
        i = N - 2

        while i >= 0:
            jump = nums[i]

            minjumps = N
            while jump > 0:
                ij = i + jump
                if ij > N - 1:
                    continue

                minjumps = min(minjumps, jump + memo[i + jump])
                jump = jump - 1

            memo[i] = minjumps

            i = i - 1

        return 0 in memo and memo[0]


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.jump
    check_solution_simple(
        sf,
        args=[[2, 3, 1, 1, 4]],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=[[2, 3, 0, 1, 4]],
        expected=2,
    )
