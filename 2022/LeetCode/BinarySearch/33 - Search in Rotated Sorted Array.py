from typing import List

# https://leetcode.com/problems/search-in-rotated-sorted-array/
DEBUG = True


def printf(s):
    global DEBUG
    if DEBUG:
        print(s)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        printf(f"--- Search: {target} in {nums}")
        rot = self.find_rotate(nums)

        if rot == 0:
            # no rotation
            printf(f" --> No Rotation")
            return self.find_target(0, len(nums) - 1, nums, target)

        # rotated along rot, so figure out which half to search
        if target < nums[0]:
            # target is in second half
            printf(f" --> Second Half Rot: {rot}")
            return self.find_target(rot, len(nums) - 1, nums, target)

        # target is in first half
        printf(f" --> First Half Rot: {rot}")
        return self.find_target(0, rot, nums, target)

    def find_rotate(self, nums: List[int]) -> int:
        """
        Find the Rotation Pivot if it exists.

        In general the array is such that n < n+1 < n+2 < ...

        So we want to search for an instance such that n-1 > n < n+1 < ... aka find 'n', the smallest value in the
        array


        If we find n such that n-1 > n < n+1, and given length of array as L(arr) then our pivot would be...
        L(arr) - index(n)
        """
        printf(f"\tFind Rot: {nums}")
        if nums[0] <= nums[-1]:
            # if the first element is <= than the last one, entire array should be in order
            return 0

        i = 0
        j = len(nums) - 1

        while i <= j:
            pivot = (i + j) // 2

            printf(f"\t\t -> i:{i} j:{j} pivot:{pivot} nums:{nums}")

            cur = nums[pivot]

            if cur > nums[pivot + 1]:
                return pivot + 1

            if cur < nums[i]:
                j = pivot - 1
            else:
                i = pivot + 1
        return 0

    def find_target(self, i, j, nums: List[int], target: int) -> int:
        printf(f"\tFind Targ: i:{i} j:{j} nums:{nums}")

        while i <= j:
            pivot = (i + j) // 2

            printf(f"\t\t -> i:{i} j:{j} pivot:{pivot} targ:{target} nums:{nums}")

            cur = nums[pivot]

            if cur == target:
                return pivot

            if target < cur:
                j = pivot - 1
            else:
                i = pivot + 1
        return -1


if __name__ == "__main__":
    s = Solution()

    def checkSolution(nums, target, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.search(nums, target)
        assert r == expected, msg.format(expected, r)

    # checkSolution(nums=[4, 5, 6, 7, 0, 1, 2], target=0, expected=4)
    # checkSolution(nums=[4, 5, 6, 7, 0, 1, 2], target=3, expected=-1)
    checkSolution(nums=[1], target=0, expected=-1)
    # checkSolution(nums=[1, 3], target=0, expected=-1)
