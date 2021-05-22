"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/283/
"""
from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
      return []
    
    o = [] 
    lookup = {} # val -> [[i, j], ...] such that nums[i]+nums[j] = val
      
    i = j = k = 0
    while i < len(nums):
      ci = nums[i]
      
      if -ci in lookup:
        # we already did this one
        continue
      
      
      
      i = i + 1
    
    return o
  
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    pass
  
if __name__ == '__main__':
  s = Solution()
  
  def compare(out, exp):
    val = False
    
    if len(out) != len(exp):
      pc(out, exp, val)
      return
    
    i = 0
    j = 0
    
    o = list(out)
    e = list(exp)
    while i < len(out):
      ci = sorted(out.pop())
      
      j = 0
      found = False
      while j < len(exp):
        cj = sorted(exp[j])
        
        if ci == cj:
          found = True
          del exp[j]
          break
      
      if not found:
        break
    val = True
    
    pc(o, e, val)
    
  def pc(out, exp, val):
    print(f"{out} == {exp} -> {val}")
  
  compare(s.threeSum([]), [])
  compare(s.threeSum([0]), [])
  compare(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])