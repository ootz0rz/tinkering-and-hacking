"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3009/
"""
WHITESPACE = ' '
NEG = '-'
POS = '+'

CLAMP_LOW = -2**31
CLAMP_HIGH = 2**31 - 1

class Solution:
  def myAtoi(self, str: str) -> int:    
    val = 0
    
    if (len(str) == 0):
      return val
    
    i = 0
    
    # skip all whitespace
    while str[i] == WHITESPACE:
      i += 1
      
      if i >= len(str):
        return val
      
    # check for pos/neg signs
    isNeg = False
    if str[i] == NEG:
      isNeg = True
      i += 1
    elif str[i] == POS:
      isNeg = False
      i += 1
      
    if i >= len(str):
      return val
    
    # convert to int
    o = ord(str[i])
    while (o >= 48) and (o <= 57):
      val *= 10
      val += o - 48
      
      i += 1
      if (i >= len(str)):
        break
      
      o = ord(str[i])          
    
    # negative val?
    if isNeg:
      val *= -1
      
    # clamp and return
    return max(min(val, CLAMP_HIGH), CLAMP_LOW)
  
if __name__ == '__main__':
  s = Solution()
  
  assert s.myAtoi("42") == 42
  assert s.myAtoi("   -42") == -42
  assert s.myAtoi("4193 with words") == 4193
  assert s.myAtoi("words and 987") == 0
  assert s.myAtoi("-91283472332") == -2147483648
  assert s.myAtoi("91283472332") == 2147483647
  assert s.myAtoi("+-12") == 0
  assert s.myAtoi("00000-42a1234") == 0