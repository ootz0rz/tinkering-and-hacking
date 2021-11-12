# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/263/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        print(f"\n\n--------\nADD: [{a}] + [{b}]")

        i = len(a) - 1
        j = len(b) - 1
        carry = "0"

        out_str = ""

        while i >= 0 or j >= 0:
            print(f"i[{i}] j[{j}] carry[{carry}] out_str[{out_str}]")

            if i >= 0 and j >= 0:
                b1 = a[i]
                b2 = b[j]

                print(f"i[{i}] >= 0 and j[{j}] >= 0 ==> b1[{b1}] b2[{b2}]")

                if b1 == "0":
                    if b2 == "0":
                        print(f"1\t b1[{b1}] b2[{b2}] out_str[{out_str}] = carry[{carry}] + out_str, carry = 0")
                        out_str = carry + out_str
                        carry = "0"
                    elif b2 == "1":
                        print(f"2\t b1[{b1}] b2[{b2}] out_str[{out_str}] = carry[{carry}] + out_str, carry = 1")
                        out_str = carry + out_str
                        carry = "0"
                elif b1 == "1":
                    if b2 == "0":
                        print(f"3\t b1[{b1}] b2[{b2}] out_str[{out_str}] = carry[{carry}] + out_str, carry = 1")
                        out_str = carry + out_str
                        carry = "1"
                    else:
                        print(f"4\t b1[{b1}] b2[{b2}] out_str[{out_str}] = carry[{carry}] + out_str, carry = 0")
                        out_str = carry + out_str
                        carry = "0"
            elif i >= 0:
                b1 = a[i]
                print(f"i[{i}] >= 0 ==> b1[{b1}]")

                if carry == "1":
                    if b1 == "1":
                        print(f"5\t b1[{b1}] out_str[{out_str}] = carry[{carry}] + out_str, carry = 1")
                        out_str = carry + out_str
                        carry = "1"
                    else:
                        print(f"6\t b1[{b1}] out_str[{out_str}] = carry[{carry}] + out_str, carry = 0")
                        out_str = carry + out_str
                        carry = "0"
                else:
                    print(f"7\t b1[{b1}] out_str[{out_str}] = b1[{b1}] + out_str")
                    out_str = b1 + out_str
            elif j >= 0:
                b2 = b[j]
                print(f"j[{j}] >= 0 ==> b2[{b2}]")

                if carry == "1":
                    if b2 == "1":
                        print(f"8\t b2[{b2}] out_str[{out_str}] = carry[{carry}] + out_str, carry = 1")
                        out_str = carry + out_str
                        carry = "1"
                    else:
                        print(f"9\t b2[{b2}] out_str[{out_str}] = carry[{carry}] + out_str, carry = 0")
                        out_str = carry + out_str
                        carry = "0"
                else:
                    print(f"0\t b2[{b2}] out_str[{out_str}] = b1[{b2}] + out_str")
                    out_str = b2 + out_str

            i = i - 1
            j = j - 1

        if carry == "1":
            print(f"\tleft over carry...")
            out_str = carry + out_str

        print(f"\t --> out: {out_str}")
        return out_str


if __name__ == '__main__':
    s = Solution()

    assert s.addBinary("0", "0") == "0"
    assert s.addBinary("0", "1") == "1"
    assert s.addBinary("1", "0") == "1"
    assert s.addBinary("1", "1") == "10"
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
