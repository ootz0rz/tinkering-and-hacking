# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3013/
from collections import deque

dop = True
class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        # if dop: print(f"\n-------\n{num1} x {num2}")
        if num1 == "0" or num2 == "0":
            # if dop: print(f'==> out[0]')
            return "0"

        big = num1
        small = num2
        if len(num2) > len(num1):
            big = num2
            small = num1

        sidx = slen = len(small)
        bidx = blen = len(big)
        out_chars = deque()
        while sidx > 0:
            schar = small[sidx - 1]
            sint = ord(schar) - 48

            bidx = blen
            while bidx > 0:
                bchar = big[bidx - 1]
                bint = ord(bchar) - 48



                bidx -= 1

            sidx -= 1

        pass

if __name__ == '__main__':
    s = Solution()

    # assert s.multiply("0", "123") == "0"
    # assert s.multiply("123", "0") == "0"
    # assert s.multiply("2", "3") == "6"
    # assert s.multiply("9", "9") == "81"
    # assert s.multiply("1", "10") == "10"
    # assert s.multiply("123", "456") == "56088"
    # assert s.multiply("9", "99") == "891"
    # assert s.multiply("999", "999") == "998001"