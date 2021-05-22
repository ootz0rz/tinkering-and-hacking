# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3011/

# attempt two because the wording on this sucks... 
# seems like they expect all elements to remain, and the "length" returned at
# end lets you say, hey ignore everything in the modified array after that idx

from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    l = len(nums)
    
    if l == 0:
      return 0
    
    i = 0
    j = 1
    
    ci = nums[i]
    while j < l:
      cj = nums[j]
      
      if cj != ci:
        i = i + 1
        ci = nums[i] = cj
      
      j = j + 1
    
    return i + 1
  
if __name__ == "__main__":
  s = Solution()
  
  assert s.removeDuplicates([1,1]) == 1
  assert s.removeDuplicates([1,1,2]) == 2
  assert s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5