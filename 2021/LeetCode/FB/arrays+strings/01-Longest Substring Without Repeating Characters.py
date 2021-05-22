"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3008/
"""
class Solution:
  """
  Given a string s, find the length of the longest substring without repeating characters.
  """
  def lengthOfLongestSubstring(self, s: str) -> int:
    maxLen = 0
    
    for idx in range(len(s)):
      chars = set([s[idx]])
      
      dist = 1
      for j in range(idx + 1, len(s)):
        c = s[j]
        
        if (c in chars):
          break
        
        chars |= {c}
        dist += 1
        
      if (dist > maxLen):
          maxLen = dist
    
    return maxLen

if __name__ == '__main__':
  s = Solution()
  
  assert s.lengthOfLongestSubstring("abcabcbb") == 3
  assert s.lengthOfLongestSubstring("bbbbb") == 1
  assert s.lengthOfLongestSubstring("pwwkew") == 3
  assert s.lengthOfLongestSubstring("") == 0