# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3013/
from collections import deque

dop = True
class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if dop: print(f"\n-------\n{num1} x {num2}")
        if num1 == "0" or num2 == "0":
            if dop: print(f'==> out[0]')
            return "0"

        big = num1
        small = num2
        if len(num2) > len(num1):
            big = num2
            small = num1

        slen = len(small)
        out_chars = deque()
        carry = 0
        place = 0
        while slen > 0:
            schar = small[slen - 1]
            sint = ord(schar) - 48

            blen = len(big)
            carry = 0

            cur_chars = deque(deque([0] * place))
            while blen > 0:
                bchar = big[blen - 1]
                bint = ord(bchar) - 48

                print_old_carry = carry
                multi = (sint * bint) + carry
                if multi >= 10:
                    carry = multi // 10  # can use // since multi <= 81
                    multi %= 10
                else:
                    carry = 0

                cur_chars.appendleft(multi)

                if dop: print(f"slen: {slen} blen: {blen} place:{[0] * place} sint[{sint}] bint[{bint}] => {sint}x{bint}=[{sint * bint} + {(print_old_carry * 10)}] multi[{multi}] + carry[{carry}] => cur_chars[{cur_chars}]")

                blen -= 1

            cur_val = 0
            cur_len = len(cur_chars)
            if cur_len > 0:
                p = 0
                while cur_len > 0:
                    cur_val += cur_chars[cur_len - 1] * (10**p)

                    cur_len -= 1
                    p += 1

            out_chars.append(cur_val)
            slen -= 1
            place += 1

        if carry > 0:
            place += len(big) - len(small)
            if dop: print(f'carry > 0 => blen[{len(big)}] slen[{len(small)}] carry[{carry}] place[{place}->{10**place}]')
            out_chars.appendleft(carry * (10**(place)))

        final_val = 0
        for v in out_chars:
            final_val += v

        if dop: print(f'final_val: {final_val}')

        final_str = ''
        v = final_val
        while v > 0:
            print_v = v

            cur_digit = v % 10
            v = v // 10
            final_str = chr(cur_digit + 48) + final_str

            if dop: print(f'v: {print_v} cur_digit[{cur_digit}] vnow[{v}] final_str[{final_str}]')

        if dop: print(f'==> final_val[{final_val}] final_str[{final_str}] out[{out_chars}]')

        return final_str

if __name__ == '__main__':
    s = Solution()

    # assert s.multiply("0", "123") == "0"
    # assert s.multiply("123", "0") == "0"
    # assert s.multiply("2", "3") == "6"
    # assert s.multiply("9", "9") == "81"
    # assert s.multiply("1", "10") == "10"
    # assert s.multiply("123", "456") == "56088"
    # assert s.multiply("9", "99") == "891"
    assert s.multiply("999", "999") == "998001"
