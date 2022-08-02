# https://leetcode.com/problems/house-robber-ii/

from typing import List, Optional, Dict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]

            j = j + 1

        return i + 1


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.removeDuplicates

    def custom_compare(args, res, expected, msg):
        l, arr = expected

        assert res == l, msg.format(l, res)

        nums = args[0]

        for i, val in enumerate(nums):
            if i >= l:
                break
            assert (
                val == arr[i]
            ), f"Expected value {arr[i]} at idx {i} but got {val}. R: {nums} E: {arr}"

    check_solution_custom(
        sf, args=[[1, 1, 2]], expected=[2, [1, 2]], custom_compare=custom_compare
    )

    check_solution_custom(
        sf,
        args=[[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]],
        expected=[5, [0, 1, 2, 3, 4]],
        custom_compare=custom_compare,
    )
