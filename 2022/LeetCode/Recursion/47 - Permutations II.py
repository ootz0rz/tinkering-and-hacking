# https://leetcode.com/problems/permutations-ii/

from typing import List, Optional


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        genset = []
        n = len(nums)

        numcount = {}
        for e in nums:
            if e not in numcount:
                numcount[e] = 1
            else:
                numcount[e] = numcount[e] + 1

        # print(f"Num Count: {numcount}")

        def gen(counts, path=[]):
            nonlocal nums, genset

            # print(f"\tgen path[{len(path)}=={n}]:{path} counts:{counts}")

            if len(path) == n:
                genset.append(path)
                return

            for k in counts:
                v = counts[k]

                """
                The idea is we use 'counts' to keep track of which items we've already used at the current iteration
                within the recursive step. If an item has a v==0, then we've used all instances of it, so we don't 
                bother to make a new permutation with it.

                So below, when we "use up" a count as we recurse, we decrement it by 1. This will go all the way through
                along the recursion until all letters get used up. This should happen when len(path) == n. 
                
                We restore the count value once we come back from the recursive step so that, for the next letter k in
                counts, it doesn't count that previous older k as being used already. 
                
                Note: an alternative way to do this would be to push the 'nums' down at each step, but remove the letter
                that got used at the current step. So the remaining nums is all the leftover letters. This is probably
                more intuitive and I think it's basically what I was doing when generating a tree by hand for all 
                permutations?
                """

                # print(f"\t\tk {k} v {v}")
                if v == 0:
                    continue

                counts[k] = v - 1
                gen(counts, path + [k])
                counts[k] = v

        gen(numcount)

        return genset


if __name__ == "__main__":
    s = Solution()

    def checkSolution(nums, expected, msg="Expected `{0}` but got `{1}`"):
        print(f"\n\n----- input: {nums}")

        r = s.permuteUnique(nums)

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
        nums=[1],
        expected=[[1]],
    )

    checkSolution(
        nums=[1, 1],
        expected=[[1, 1]],
    )

    checkSolution(
        nums=[1, 2],
        expected=[[1, 2], [2, 1]],
    )

    checkSolution(
        nums=[1, 1, 2],
        expected=[[1, 1, 2], [1, 2, 1], [2, 1, 1]],
    )
