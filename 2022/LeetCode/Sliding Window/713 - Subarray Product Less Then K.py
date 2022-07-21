from typing import List


"""
# This works but is way too slow

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        print(f"--- Start {nums} < {k}")
        results = 0
        window_size = 0  # start at 1, go until len(nums)

        i = 0
        while window_size <= len(nums):
            j = i + window_size

            print(f"i:{i} j:{j} window_size:{window_size}")

            if j >= len(nums):
                i = 0
                window_size += 1
                continue

            prod = 1
            n = []
            while j >= i:
                n.append(nums[j])
                prod *= nums[j]
                j -= 1

            if prod < k:
                print(f"\t\tResult += 1: {n}={prod} < {k}")
                results += 1
            else:
                print(f"\t\tFailed: {n}={prod} < {k}")

            i += 1

        return results
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        # print(f"___ START___ {nums} < k:{k}")
        result = 0

        if k <= 1:
            return result

        product = 1
        left = 0
        for right, rval in enumerate(nums):
            product = product * rval

            while product >= k:
                product /= nums[left]
                left = left + 1

            result += right - left + 1

        return result


if __name__ == "__main__":
    sol = Solution()

    def checkSolution(nums, k, expected, msg="Expected `{0}` but got `{1}`"):
        r = sol.numSubarrayProductLessThanK(nums, k)
        # assert r == expected, msg.format(expected, r)

    checkSolution(nums=[10, 5, 2, 6], k=100, expected=8)
