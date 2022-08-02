from typing import List, Optional


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # print(f"--- nums: {nums}")

        genset = [[]]
        nums.sort()

        # note: having the gen function in here is fucking ugly but leetcode was throwing all sorts of random errors
        # when i didnt.... so dumb -.-
        def gen(curlen, seen={}):
            nonlocal genset, nums
            # print(
            #     f"\tGen Call <nums:{nums}> <curlen:{curlen}> genset<{genset}> seen<{seen}>"
            # )
            if len(nums) == curlen:
                return

            i = 0
            n = len(genset)
            c = nums[curlen]

            # see note below
            if c in seen:
                i = seen[c]

            # print(
            #     f"\t\tC = {c}, seen? {(c in seen)} => genset[i:{i}, n:{n}]={genset[i:n]}"
            # )

            c_i = len(genset)
            while i < n:
                e = genset[i]
                i = i + 1
                # print(f"\t\t\tGen[{i}]={e} of {genset}")

                g = list(e) + [c]
                genset.append(g)
            c_n = len(genset)

            # the idea is every time we've seen a value, we track the range of new subsets that we added with it...
            # so next time around, if we find a duplicate, we only add the dupe value to these generated subsets and none
            # of the others
            #
            # note that we sorted the nums array first, to make sure all duplicates happen one after another
            seen[c] = c_i
            # print(f"\t\tseen add[{c}] => {seen[c]}")

            gen(curlen + 1)

        gen(0)

        return genset


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.subsetsWithDup
    check_solution_as_sets(
        sf,
        args=[[1, 2, 2]],
        expected=[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
        output_set_transform=map_to_tuple_set,
        expected_set_transform=map_to_tuple_set,
    )
