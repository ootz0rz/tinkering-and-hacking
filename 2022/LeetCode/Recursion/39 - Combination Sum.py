# https://leetcode.com/problems/combination-sum/

from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []

        """
        The basic idea is that we generate a tree where the left-most side is trying to use as many small values to add
        up to the target, k, as possible. As you go down and to the right along that tree, you start adding the next
        larget value, and the next, etc... to build the set of sums
        
        Note that this assumes the input candidates is sorted already. This seems to be the case with the leetcode test
        cases but it wasn't specifically mentioned.
        """
        # print(f"Candidates: {candidates} k={target}")

        def gen(path, remainder, i):
            nonlocal candidates, solutions

            # print(f"\tCur Path: {path}, k={remainder}, i={i}")

            if remainder == 0:
                # print(f"\t -> Add Path: {path}")
                solutions.append(path[:])
                return

            if remainder < 0:
                return

            for idx, c in enumerate(candidates[i:]):
                # print(
                #     f"\t\t Add {c}, nk={remainder-c}, ni={idx+i}, current cands: {candidates[i:]}"
                # )
                gen(path + [c], remainder - c, idx + i)

        gen([], target, 0)

        return solutions


if __name__ == "__main__":
    s = Solution()

    def checkSolution(candidates, target, expected, msg="Expected `{0}` but got `{1}`"):
        print(f"\n\n----- input: {candidates}, {target}")

        r = s.combinationSum(candidates, target)

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
    #     candidates=[2, 3, 6, 7],
    #     target=7,
    #     expected=[[2, 2, 3], [7]],
    # )

    checkSolution(
        candidates=[2, 3, 5],
        target=8,
        expected=[[2, 2, 2, 2], [2, 3, 3], [3, 5]],
    )
