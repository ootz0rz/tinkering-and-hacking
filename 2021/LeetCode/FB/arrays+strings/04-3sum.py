"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/283/
"""
from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
      return []
    
    o = [] 
    lookup = {} # val -> idx
    
    # gen lookup table
    for idx,v in enumerate(nums):
      lookup[nums[idx]] = idx
      
    i = j = k = 0
    used = []
    while i < len(nums):
      ci = nums[i]
      
      j = i + 1
      while j < len(nums):
        cj = nums[j]
      
        k = j + 1
        while k < len(nums):
          ck = nums[k]
          if (ci + cj + ck) == 0:
            idxset = set({i, j, k})
            
            # is this triplet already used?
            if idxset in used:
              k = k + 1
              continue
            
            used.append(idxset)
            
            sol = sorted([ci, cj, ck])
            print(f"nums: {nums} -> used:{used} -> idxset:{idxset} == {sol}")
            
            if not (sol in o):
              o.append(sol)
            
          k = k + 1
          
        j = j + 1
      
      i = i + 1
    
    return o
  
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
      ci = out.pop()
      
      j = 0
      found = False
      while j < len(exp):
        cj = exp[j]
        
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