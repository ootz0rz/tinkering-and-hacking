# https://leetcode.com/problems/combination-sum-ii/

from typing import List, Optional, Dict


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Similar to #39, but this time we don't reuse elements. However there may be duplicates within the input set
        itself.

        In this case, it seems the leet code tests will not have sorted input. So we can sort them first, and then skip
        over duplicates as they come up. It's important to note that we only skip duplicates that come AFTER our current
        candidate. This way, we can still use duplicate candidates if they are in the original input, but avoid dupe
        output.
        """

        solutions = []
        candidates.sort()

        def gen(path: List[int], remainder: int, i: int):
            nonlocal candidates, solutions

            if remainder == 0:
                solutions.append(path)
                return

            if remainder < 0:
                return

            for idx in range(i, len(candidates)):
                c = candidates[idx]

                if idx > i and c == candidates[idx - 1]:
                    # this is how we skip subsequent dupes, but make sure we always use up the 'current' candidate
                    # basically, make sure we're not the same as our previous value
                    continue

                # since candidates is sorted, if the current candidate makes the remainder < 0, no need to process it
                # nor anything that comes after it
                rc = remainder - c
                if rc < 0:
                    break

                gen(path + [c], rc, idx + 1)

        gen([], target, 0)

        return solutions


if __name__ == "__main__":
    s = Solution()

    def checkSolution(candidates, target, expected, msg="Expected `{0}` but got `{1}`"):
        print(f"\n\n----- input: {candidates}, {target}")

        r = s.combinationSum2(candidates, target)

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

    # checkSolution(
    #     candidates=[10, 1, 2, 7, 6, 1, 5],
    #     target=8,
    #     expected=[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
    # )

    checkSolution(
        candidates=[2, 5, 2, 1, 2],
        target=5,
        expected=[[1, 2, 2], [5]],
    )
