# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List, Optional, Dict

MAPPING = {
    "2": list("abc"),
    "3": list("def"),
    "4": list("ghi"),
    "5": list("jkl"),
    "6": list("mno"),
    "7": list("pqrs"),
    "8": list("tuv"),
    "9": list("wxyz"),
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        solution = []

        if len(digits) == 0:
            return solution

        def gen(path, i):
            if len(path) == len(digits):
                solution.append(path)
                return

            for idx, d in enumerate(digits[i:]):
                for m in MAPPING[d]:
                    gen(path + m, i + idx + 1)

        gen("", 0)

        return solution


if __name__ == "__main__":
    s = Solution()

    def checkSolution(digits, expected, msg="Expected `{0}` but got `{1}`"):
        print(f"\n\n----- input: {digits}")

        r = s.letterCombinations(digits)

        assert len(r) == len(
            expected
        ), f"Expected outut len {len(expected)} but got {len(r)}. Expected: {expected} Result: {r}"

        # https://stackoverflow.com/questions/6105777/how-to-compare-a-list-of-lists-sets-in-python
        rset = set(map(tuple, r))
        eset = set(map(tuple, expected))

        diff = rset.symmetric_difference(eset)

        print(f"r: {rset} v e: {eset}")
        assert (
            len(diff) == 0
        ), f"Expected no differences, but got {len(diff)}:{diff} vs {len(eset)}:{eset}"

        print("Completed test case.")

    checkSolution(
        digits="2",
        expected=list("abc"),
    )

    checkSolution(
        digits="23",
        expected=["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
    )
