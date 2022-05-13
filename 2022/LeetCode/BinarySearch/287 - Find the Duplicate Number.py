from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # based on Floyd's https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
        T = nums[0]
        H = nums[0]

        while True:
            T = nums[T]
            H = nums[nums[H]]

            if T == H:
                break

        T = nums[0]
        while T != H:
            T = nums[T]
            H = nums[H]

        return H
