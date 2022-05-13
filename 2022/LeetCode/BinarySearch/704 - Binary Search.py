from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            pivot = (i + j) // 2
            cur = nums[pivot]

            if cur == target:
                return pivot
            elif cur < target:
                i = pivot + 1
            else:
                j = pivot - 1

        return -1
