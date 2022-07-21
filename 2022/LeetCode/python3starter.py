from typing import List


if __name__ == "__main__":
    sol = Solution()

    def checkSolution(nums, target, expected, msg="Expected `{0}` but got `{1}`"):
        r = sol.searchRange(nums, target)
        print(flush=True)
        assert r == expected, msg.format(expected, r)

    checkSolution(nums=[5, 7, 7, 8, 8, 10], target=8, expected=[3, 4])
