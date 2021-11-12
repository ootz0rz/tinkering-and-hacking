# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/263/
debug = False

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        global debug

        if debug: print(f"\n\n--------\nADD: [{a}] + [{b}]\n\n")

        i = len(a) - 1
        j = len(b) - 1
        carry = "0"

        out_str = ""

        ri = -1
        r = ""
        while i >= 0 or j >= 0 or ri >= 0:
            if i >= 0 or j >= 0:
                if debug: print(f"i[{i}] j[{j}] ri[{ri}] carry[{carry}] out[{out_str}]")
            else:
                if debug: print(f"ri[{ri}] carry[{carry}] out[{out_str}]")

            if i >= 0 and j >= 0:
                b1 = a[i]
                b2 = b[j]

                if debug: print(f"\t0 b1[{b1}] + b2[{b2}] + carry[{carry}] | out_str[{out_str}]")
                if b1 == "1" and b2 == "1":
                    out_str = (carry if carry == "1" else "0") + out_str
                    if debug: print(f"\t--> 1+1 + [{carry}] | out_str[{out_str}]")
                    carry = "1"
                elif b1 == "0" and b2 == "0":
                    out_str = (carry if carry == "1" else "0") + out_str
                    if debug: print(f"\t--> 0+0 + [{carry}] | out_str[{out_str}]")
                    carry = "0"
                else:
                    out_str = ("0" if carry == "1" else "1") + out_str
                    if debug: print(f"\t--> 1+0 + [{carry}] | out_str[{out_str}]")
                    carry = carry
            elif i >= 0:
                ri = i
                r = a
                if debug: print(f"\tA -> R [{r}] + carry[{carry}] | out_str[{out_str}]")

                i = -1
            elif j >= 0:
                ri = j
                r = b
                if debug: print(f"\tB -> R [{r}] + carry[{carry}] | out_str[{out_str}]")

                j = -1

            if ri >= 0:
                rb = r[ri]
                if carry == "0":
                    out_str = rb + out_str
                    if debug: print(f"\t-->1 rb[{rb}] carry[{carry}] | out_str[{out_str}]")
                elif carry == "1":
                    if rb == "1":
                        out_str = "0" + out_str
                        carry = "1"
                        if debug: print(f"\t-->2 rb[{rb}] carry[{carry}] | out_str[{out_str}]")
                    else:
                        out_str = carry + out_str
                        carry = "0"
                        if debug: print(f"\t-->3 rb[{rb}] carry[{carry}] | out_str[{out_str}]")
                ri = ri - 1

            i = i - 1
            j = j - 1

        if debug: print(f"00 i[{i}] + j[{j}] + carry[{carry}] | out_str[{out_str}]")

        if carry == "1":
            if debug: print(f"\t leftover carry: {carry}")
            out_str = carry + out_str

        if debug: print(f"\t --> out: {out_str}")
        return out_str


if __name__ == '__main__':
    debug = False

    s = Solution()

    assert s.addBinary("0", "0") == "0"
    assert s.addBinary("0", "1") == "1"
    assert s.addBinary("1", "0") == "1"
    assert s.addBinary("1", "1") == "10"
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    assert s.addBinary("1", "111") == "1000"
    assert s.addBinary("10", "101111") == "110001"
    assert s.addBinary("110010", "10111") == "1001001"
