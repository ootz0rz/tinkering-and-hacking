# https://leetcode.com/problems/subsets/

from typing import List, Optional


def gen(nums, curlen, genset):
    if len(nums) == curlen:
        return

    n = set()
    for e in genset:
        g = frozenset(list(e) + [nums[curlen]])
        n.add(g)

    genset.update(n)
    gen(nums, curlen + 1, genset)


# genset = set([frozenset()])
# gen([1,2,3], 0, genset)
# print(f"End: {genset}")


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        genset = set([frozenset()])
        gen(nums, 0, genset)

        o = []
        for i, e in enumerate(genset):
            o.append(list(e))

        return o


if __name__ == "__main__":
    s = Solution()

    def checkSolution(nums, expected, msg="Expected `{0}` but got `{1}`"):
        print(f"\n\n----- nums: {nums}")

        r = s.subsets(nums)

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
        nums=[1, 2, 3],
        expected=[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
    )
