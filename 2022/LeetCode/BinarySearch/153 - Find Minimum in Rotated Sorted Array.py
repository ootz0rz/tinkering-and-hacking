from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            # entire array should be sorted so just return first element
            return nums[0]

        i = 0
        j = len(nums) - 1

        while i <= j:
            pivot = (i + j) // 2
            cur = nums[pivot]

            if cur > nums[pivot + 1]:
                return nums[pivot + 1]

            if cur < nums[i]:
                j = pivot - 1
            else:
                i = pivot + 1

        return -1


if __name__ == "__main__":
    s = Solution()

    def checkSolution(nums, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.findMin(nums)
        assert r == expected, msg.format(expected, r)

    checkSolution(nums=[3, 4, 5, 1, 2], expected=1)
    checkSolution(nums=[4, 5, 6, 7, 0, 1, 2], expected=0)
    checkSolution(nums=[11, 13, 15, 17], expected=11)
