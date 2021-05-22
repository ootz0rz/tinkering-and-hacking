# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3012/

from typing import List

class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    print(f"\n{'#'*20}")
    print(f"{'#'*5} {nums}")
    
    if len(nums) <= 1:
      return
    
    i = len(nums) - 1
    j = i - 1
    
    didFind = False
    while i >= 0 and j >= 0:
      if nums[j] < nums[i]:
        didFind = True
        nums[j] = nums[i]
        break
      
      i = i - 1
      j = j - 1
      
    print(f"didFind? {didFind} nums {nums}")
  
if __name__ == '__main__':
  
  s = Solution()
  
  def check(inp, exp):
    global s
    v = list(inp)
    
    s.nextPermutation(v)
    
    st = f"Input<{inp}> Expected<{exp}> Got<{v}>"
    print(st)
    assert v == exp, st
  
  check([1], [1])
  check([1,2,3], [1,3,2])
  check([1,2,3,4], [1,2,4,3])
  check([3,2,1], [1,2,3])