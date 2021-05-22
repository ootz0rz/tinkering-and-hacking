"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3010/
"""

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

switch = {
  "I" : I,
  "V" : V,
  "X" : X,
  "L" : L,
  "C" : C,
  "D" : D,
  "M" : M,
  
  "IV": V - I,
  "IX": X - I,
  
  "XL" : L - X,
  "XC" : C - X,
  
  "CD" : D - C,
  "CM" : M - C,
}

class Solution:
  def romanToInt(self, s: str) -> int:
    val: int = 0
      
    i = 0
    while i < len(s):     
      c = s[i]
      
      if (i + 1) < len(s):
        cn = s[i + 1]
      else:
        cn = ""
      
      # check for substraction exceptions
      if len(cn) > 0 and (
          (c == "I" and (cn == "V" or cn == "X")) \
          or (c == "X" and (cn == "L" or cn == "C")) \
          or (c == "C" and (cn == "D" or cn == "M"))):
        c = c + cn
        i = i + 1
        
      cval = switch.get(c)
      
      val = val + cval
      
      i = i + 1
    
    return val
  
if __name__ == '__main__':
  s = Solution()
  assert s.romanToInt("") == 0
  
  assert s.romanToInt("I") == 1
  assert s.romanToInt("V") == 5
  assert s.romanToInt("X") == 10
  assert s.romanToInt("L") == 50
  assert s.romanToInt("C") == 100
  assert s.romanToInt("D") == 500
  assert s.romanToInt("M") == 1000
  
  assert s.romanToInt("IV") == 4
  assert s.romanToInt("VI") == 6
  assert s.romanToInt("IX") == 9
  assert s.romanToInt("XI") == 11
  
  assert s.romanToInt("XL") == 40
  assert s.romanToInt("LX") == 60
  assert s.romanToInt("XC") == 90
  assert s.romanToInt("CX") == 110
  
  assert s.romanToInt("CD") == 400
  assert s.romanToInt("DC") == 600
  assert s.romanToInt("CM") == 900
  assert s.romanToInt("MC") == 1100
  
  assert s.romanToInt("III") == 3
  assert s.romanToInt("LVIII") == 58
  assert s.romanToInt("MCMXCIV") == 1994