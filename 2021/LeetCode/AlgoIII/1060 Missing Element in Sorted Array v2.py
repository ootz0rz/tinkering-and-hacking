# https://leetcode.com/problems/missing-element-in-sorted-array/

from typing import *

debug = False
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        global debug

        if debug: print(f'\nk={k} on {nums}')

        def num_miss(idx: int) -> int:
            return Solution.num_missing(nums, idx)

        n = len(nums)
        total_missing_in_bounds = num_miss(n - 1)

        # cases:
        # 1:  k > bounds
        if k > total_missing_in_bounds:
            if debug: print(f'\t [0] k<{k}> - total_missing_in_bounds<{total_missing_in_bounds}> + nums[-1]<{nums[-1]}>')
            return k - total_missing_in_bounds + nums[-1]

        # 2:  k within bounds

        # lets find a pivot point such that num_missing(lidx) >= k
        # so we pick a pivot between left and right ends of the array,
        # and move the left gradually upwards
        lidx = 0
        ridx = n - 1
        while lidx != ridx:
            pivot = lidx + ((ridx - lidx) // 2)

            if num_miss(pivot) >= k:
                ridx = pivot
            else:
                lidx = pivot + 1

        if debug: print(f'\t [1] k<{k}> - num_miss(lidx - 1)<{num_miss(lidx - 1)}> + nums[lidx - 1]<{nums[lidx - 1]}>')
        return k - num_miss(lidx - 1) + nums[lidx - 1]

    @staticmethod
    def num_missing(arr: List[int], idx: int) -> int:
        # note that we can calculate the num missing at any idx by looking at...
        # val[idx] - val[0] - idx
        # this is because idx => # of values we actually have up to that point
        return arr[idx] - arr[0] - idx


if __name__ == '__main__':
    debug = True
    s = Solution()

    assert s.missingElement([4, 7, 9, 10], 1) == 5
    assert s.missingElement([4, 7, 9, 10], 7) == 14
    assert s.missingElement([4, 7, 9, 10], 3) == 8
    assert s.missingElement([1, 2, 4], 3) == 6
