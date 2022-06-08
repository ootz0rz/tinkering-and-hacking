from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        processed = set()

        m = {}
        for i, targ in enumerate(nums):
            if targ in processed:
                # we've already done this value before so no need to go through the trouble again
                continue

            processed.add(targ)
            # iterate over the rest of the list
            for j, jval in enumerate(nums[i + 1 :]):
                required = -targ - jval  # value required to get to zero

                # if the amount we require to get to 0 has already been seen,
                # we check to see if it can be used for the current index i
                if required in m and m[required] == i:
                    result.add(tuple(sorted([targ, jval, required])))

                m[jval] = i  # => j is a compliment to i

        return result


if __name__ == "__main__":
    s = Solution()

    def checkSolution(nums, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.threeSum(nums)
        assert r == expected, msg.format(expected, r)

    checkSolution(
        nums=[-1, 0, 1, 2, -1, -4],
        expected=set([tuple([-1, -1, 2]), tuple([-1, 0, 1])]),
    )
