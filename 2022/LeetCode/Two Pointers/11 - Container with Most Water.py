from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest = 0
        i = 0
        j = len(height) - 1

        while i < j:
            left = height[i]
            right = height[j]
            width = j - i

            highest = max(highest, min(left, right) * width)

            if left <= right:
                i = i + 1
            else:
                j = j - 1

        return highest


if __name__ == "__main__":
    s = Solution()

    def checkSolution(nums, target, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.searchRange(nums, target)
        assert r == expected, msg.format(expected, r)

    checkSolution(nums=[5, 7, 7, 8, 8, 10], target=8, expected=[3, 4])


# https://leetcode.com/problems/container-with-most-water/
