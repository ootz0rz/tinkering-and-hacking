# https://leetcode.com/problems/missing-element-in-sorted-array/

from typing import *

debug = False
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        global debug

        if debug: print(f'\nk={k} on {nums}')

        total_missing = 0
        idx = 0

        k_val = None
        # O(n)
        while idx < len(nums) - 1:
            cur_missing = nums[idx + 1] - nums[idx] - 1

            if debug: print(f'\tk[{k}] idx[{idx}={nums[idx]}] idx+1[{idx+1}={nums[idx+1]}] cur_miss[{cur_missing}] old tot_miss[{total_missing}]')

            if (total_missing + cur_missing) >= k:
                k_val = k - total_missing + nums[idx]
                if debug: print(f'\t[0] kVal<{k_val}> = k<{k}> - total_missing<{total_missing}> + nums[idx]<{nums[idx]}>')
                break

            total_missing = total_missing + cur_missing

            idx = idx + 1

        if k_val is None:
            # k is passed nums end bound... so just calc the value it would be
            k_val = (k - total_missing) + nums[-1]
            if debug: print(f'\t[1] k_val<{k_val}> = (k<{k}> - total_missing<{total_missing}>) + nums[-1]<{nums[-1]}>')

        return k_val


if __name__ == '__main__':
    debug = True
    s = Solution()

    assert s.missingElement([4, 7, 9, 10], 1) == 5
    assert s.missingElement([4, 7, 9, 10], 7) == 14
    assert s.missingElement([4, 7, 9, 10], 3) == 8
    assert s.missingElement([1, 2, 4], 3) == 6
