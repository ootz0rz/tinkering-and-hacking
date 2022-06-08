from typing import List

BS_CHAR = "#"


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        print(f"Compare {s} v {t}")
        global BS_CHAR
        i = len(s) - 1
        j = len(t) - 1

        i_skip = 0
        j_skip = 0
        while i >= 0 or j >= 0:
            print(f"\t Start [{i}:{s[i]}]!=[{j}:{t[j]}]")
            # skip if need be
            while i >= 0:
                if s[i] == BS_CHAR:
                    print(f"\t\ti - Skip {i}:{s[i]} == #")
                    i_skip = i_skip + 1
                    i = i - 1
                elif i_skip > 0:
                    print(f"\t\ti - Skip {i}:{s[i]}, i_skip:{i_skip} >= 0")
                    i_skip = i_skip - 1
                    i = i - 1
                else:
                    break

            while j >= 0:
                if t[j] == BS_CHAR:
                    print(f"\t\tj - Skip {j}:{t[j]} == #")
                    j_skip = j_skip + 1
                    j = j - 1
                elif j_skip > 0:
                    print(f"\t\tj - Skip {j}:{t[j]}, j_skip:{j_skip} >= 0")
                    j_skip = j_skip - 1
                    j = j - 1
                else:
                    break

            print(f"\t\t Compare [{i}:{s[i]}]!=[{j}:{t[j]}] => {(s[i] == t[j])}")

            if i >= 0 and j >= 0 and s[i] != t[j]:
                # if even after doing all the skipping, we're still not the same... done our check
                print("[0] -> FALSE")
                return False

            if (i >= 0) != (j >= 0):
                # one of them didn't complete comparisons
                print("[10] -> FALSE")
                return False

            i = i - 1
            j = j - 1

        print(f"Final Tally => i:{i} j:{j}")

        print("[20] -> TRUE")
        return True


if __name__ == "__main__":
    sol = Solution()

    def checkSolution(s, t, expected, msg="Expected `{0}` but got `{1}`"):
        r = sol.backspaceCompare(s, t)
        # assert r == expected, msg.format(expected, r)

    checkSolution(s="ab#c", t="ad#c", expected=True)
    checkSolution(s="ab##", t="c#d#", expected=True)
    checkSolution(s="a#c", t="b", expected=False)
    checkSolution(s="bbbextm", t="bbb#extm", expected=False)
    checkSolution(s="nzp#o#g", t="b#nzp#o#g", expected=True)

# https://leetcode.com/problems/backspace-string-compare/
