# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3011/

from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    i = 0
    while i < len(nums):
      ci = nums[i]
      
      j = i + 1
      while j < len(nums) and nums[j] == ci:
        del nums[j]
      
      i = i + 1
      
    return len(nums)
  
if __name__ == "__main__":
  s = Solution()
  
  assert s.removeDuplicates([1,1]) == 1
  assert s.removeDuplicates([1,1,2]) == 2
  assert s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5