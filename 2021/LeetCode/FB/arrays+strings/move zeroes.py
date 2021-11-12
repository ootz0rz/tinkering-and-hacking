# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/262/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 0
        # print(f'------ nums: {nums}')
        l = len(nums)
        while j < l:
            # print(f'i[{i}] j[{j}] nums[i][{nums[i]}] nums[j][{nums[j]}] | nums: {nums}')

            if nums[j] == 0:
                j = j + 1
                continue

            if nums[i] == 0:
                nums[i] = nums[j]
                nums[j] = 0
                i = i + 1
                continue

            i = i + 1
            j = j + 1

        # print(f'# i[{i}] j[{j}] nums: {nums}')

        return nums


if __name__ == '__main__':
    s = Solution()

    def compare(l1, l3):
        if len(l1) != len(l3):
            return False

        i = 0
        while i < len(l1):
            if l1[i] != l3[i]:
                return False
            i += 1

        return True

    assert compare(s.moveZeroes([0]), [0])
    assert compare(s.moveZeroes([0, 1]), [1, 0])
    assert compare(s.moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
