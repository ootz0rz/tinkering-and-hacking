from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            pivot = (i + j) // 2

            cur = nums[pivot]

            if cur < nums[pivot + 1]:
                i = pivot + 1
            else:
                j = pivot

        return i
