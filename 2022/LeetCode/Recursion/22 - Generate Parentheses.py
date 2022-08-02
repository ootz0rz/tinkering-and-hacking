# https://leetcode.com/problems/generate-parentheses/

from typing import List, Optional, Dict


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []

        if n < 1:
            return solutions

        def gen(path, left=0, right=0):
            if left == right and left == n:
                solutions.append(path)

            if left < n:
                gen(path + "(", left + 1, right)

            if right < n and left > right:
                gen(path + ")", left, right + 1)

        gen("(", 1, 0)

        return solutions


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.generateParenthesis
    check_solution_as_sets(
        sf,
        args=[0],
        expected=[],
    )

    check_solution_as_sets(
        sf,
        args=[1],
        expected=["()"],
    )

    check_solution_as_sets(
        sf,
        args=[3],
        expected=["((()))", "(()())", "(())()", "()(())", "()()()"],
    )

    # s = Solution()

    # def checkSolution(n, expected, msg="Expected `{0}` but got `{1}`"):
    #     print(f"\n\n----- input: {n}")

    #     r = s.generateParenthesis(n)

    #     assert len(r) == len(
    #         expected
    #     ), f"Expected outut len {len(expected)} but got {len(r)}. Expected: {expected} Result: {r}"

    #     # https://stackoverflow.com/questions/6105777/how-to-compare-a-list-of-lists-sets-in-python
    #     rset = set(r)
    #     eset = set(expected)

    #     diff = rset.symmetric_difference(eset)

    #     print(f"r: {rset} v e: {eset}")
    #     assert (
    #         len(diff) == 0
    #     ), f"Expected no differences, but got {len(diff)}:{diff} vs {len(eset)}:{eset}"

    #     print("Completed test case.")

    # checkSolution(
    #     n=0,
    #     expected=[],
    # )

    # checkSolution(
    #     n=1,
    #     expected=["()"],
    # )

    # checkSolution(
    #     n=3,
    #     expected=["((()))", "(()())", "(())()", "()(())", "()()()"],
    # )
