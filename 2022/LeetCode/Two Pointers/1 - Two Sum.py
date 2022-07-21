from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, cur in enumerate(nums):
            remainder = target - cur
            if remainder in m:
                return sorted([i, m[remainder]])
            m[cur] = i


if __name__ == "__main__":
    s = Solution()

    def checkSolution(nums, target, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.twoSum(nums, target)
        assert r == expected, msg.format(expected, r)

    checkSolution(nums=[2, 7, 11, 15], target=9, expected=[0, 1])
    checkSolution(nums=[3, 2, 4], target=6, expected=[1, 2])
    checkSolution(nums=[3, 3], target=6, expected=[0, 1])
