from typing import List


MAX = float("inf")


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = MAX

        sum = 0
        left = 0
        for right, rval in enumerate(nums):
            sum = sum + rval

            while sum >= target:
                result = min(result, right - left + 1)

                sum -= nums[left]
                left = left + 1

        if result == MAX:
            return 0

        return result


if __name__ == "__main__":
    sol = Solution()

    def checkSolution(target, nums, expected, msg="Expected `{0}` but got `{1}`"):
        r = sol.minSubArrayLen(target, nums)
        print(flush=True)
        assert r == expected, msg.format(expected, r)

    checkSolution(target=7, nums=[2, 3, 1, 2, 4, 3], expected=2)
