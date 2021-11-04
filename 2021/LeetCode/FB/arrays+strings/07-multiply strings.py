# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3013/
from collections import deque

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        print(f"\n-------\n{num1} x {num2}")
        if num1 == "0" or num2 == "0":
            return "0"

        big = num1
        small = num2
        if len(num2) > len(num1):
            big = num2
            small = num1

        slen = len(small)
        blen = len(big)
        out_chars = deque([])
        carry = 0
        while slen > 0:
            schar = small[slen - 1]
            bchar = big[slen - 1]

            sint = ord(schar) - 48
            bint = ord(bchar) - 48

            print_old_carry = carry
            multi = (sint * bint) + (carry * 10)
            if multi >= 10:
                carry = multi // 10
                multi %= 10
            else:
                carry = 0

            out_chars.appendleft(chr(multi + 48))

            print(f'slen: {slen} sint[{sint}] bint[{bint}] => x[{sint * bint} + {(print_old_carry * 10)}] multi[{multi}] + carry[{carry}] => out[{("".join(list(out_chars)))}]')

            slen -= 1
            blen -= 1

        if carry > 0:
            out_chars.appendleft(chr(carry + 48))

        print(f'blen: {blen} slen: {slen}')

        if blen > 0:
            while blen > 0:
                out_chars.append("0")
                blen -= 1

        print(f'out[{("".join(list(out_chars)))}]')

        return "".join(list(out_chars))

if __name__ == '__main__':
    s = Solution()

    # assert s.multiply("0", "123") == "0"
    # assert s.multiply("123", "0") == "0"
    # assert s.multiply("2", "3") == "6"
    # assert s.multiply("9", "9") == "81"
    # assert s.multiply("1", "10") == "10"
    assert s.multiply("123", "456") == "56088"
