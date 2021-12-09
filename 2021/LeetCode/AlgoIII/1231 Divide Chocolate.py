# https://leetcode.com/problems/divide-chocolate/
from typing import *

debug = False

MAX_SWEET = 2**31-1

def _maximizeSweetness(sweetness: List[int], num_peeps: int, min_sweet: int, max_sweet: int) -> int:
    global debug

    sweetness_target = min_sweet + (max_sweet - min_sweet) // 2

    if debug: print(f'\ttarget[(max_sweet<{max_sweet}> - min_sweet<{min_sweet}>) // 2]=[{sweetness_target}]')

    # divvy into chunks
    idx = 0
    chunks = 0
    cur_chunk_val = 0
    smallest_chunk = MAX_SWEET

    sidx = 0
    eidx = 0
    while idx < len(sweetness):
        cur_val = sweetness[idx]

        cur_chunk_val = cur_chunk_val + cur_val
        # did we achieve target?
        if cur_chunk_val >= sweetness_target:
            # record smallest chunk's value
            if cur_chunk_val < smallest_chunk:
                smallest_chunk = cur_chunk_val

            eidx = idx
            if debug:
                print(f'-> chunk[{sidx}:{eidx}]: {sweetness[sidx:eidx+1]} => {cur_chunk_val}')
                sidx = idx+1

            # record chunk and move on
            chunks = chunks + 1
            cur_chunk_val = 0

        idx = idx + 1

    if debug: print(f'\t\tchunks: {chunks}, smallest: {smallest_chunk}, target: {sweetness_target}')

    if min_sweet == max_sweet:
        # nothing left to search...
        if debug: print(f'\t\t --> end of line: {min_sweet} == {max_sweet} => {-1}')
        if chunks >= num_peeps:
            return smallest_chunk
        else:
            return -1

    if chunks >= num_peeps:
        # lets check if we can bump the value higher, search right
        if debug: print(f'right: {sweetness}, num_peeps: {num_peeps}, range[{sweetness_target}, {max_sweet}]')
        right = _maximizeSweetness(sweetness, num_peeps, sweetness_target+1, max_sweet)

        if right > smallest_chunk:
            # right side was bigger!
            if debug: print(f'\t\t --> right: {right}')
            return right
        else:
            # nope, the right side don't work... so just return what we got for now
            if debug: print(f'\t\t --> smallest: {smallest_chunk}')
            return smallest_chunk

    # do we have a valid result?
    if smallest_chunk < sweetness_target or chunks < num_peeps:
        # this value is not valid, so our target is too high... search below
        if debug: print(f'left: {sweetness}, num_peeps: {num_peeps}, range[{min_sweet}, {sweetness_target-1}]')
        return _maximizeSweetness(sweetness, num_peeps, min_sweet, sweetness_target-1)

    return smallest_chunk


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        we want to optimize for the biggest chunk we can make from any slicing
        of sweetness into k+1 slices, such that the chunk is also the smallest
        from all the other chunks in that current slicing

        if k = 0, then there is only 1 slice with min sweetness = sum(sweetness)

        if k = 1, and sweetness is evenly divisible, then we know that both
        slices should be sum(sweetness)/2 each

        generalizing this a bit, if k = n, and sweetness is equally divisible
        into n+1 slices, then each slice should be sum(sweetness)/k+1

        we also know that the min for any slice is min_sweet = min(sweetness),
        which is the smallest/least-sweet any of our slices can be

        this gives us our search space [min_sweet, sum(sweetness)/k+1]

        we can then binary search through this space... choosing a pivot
        such that pivot = (sum(sweetness)/k+1) - (min_sweet) // 2

        we then start iterating through sweetness from front to back, creating
        accumulating slices in size until they are at least pivot in sweetness

        if we are able to make enough slices for k+1 people, we're good...
        otherwise this value fails

        if it works, we search above until we find the largest value that works
        if it doesn't work, we search below
        """
        num_peeps = k + 1
        min_sweet = min(sweetness)
        max_sweet = sum(sweetness) // num_peeps

        if debug: print(f'\n-----\nsweetness: {sweetness}, num_peeps: {num_peeps}, range[{min_sweet}, {max_sweet}]')

        return _maximizeSweetness(sweetness, num_peeps, min_sweet, max_sweet)


if __name__ == '__main__':
    debug = True
    s = Solution()

    # r = s.maximizeSweetness([1, 2, 3], 0)
    # print(f'{r} == {sum([1, 2, 3])}')

    # r = s.maximizeSweetness([1, 2, 2, 1, 2, 2, 1, 2, 2], 2)
    # assert r == 5

    # r = s.maximizeSweetness([5,6,7,8,9,1,2,3,4], 8)
    # print(f'{r} == {1}')

    r = s.maximizeSweetness([1,2,3,4,5,6,7,8,9], 5)
    assert r == 6

    # r = s.maximizeSweetness([87506,32090,9852,96263,52415,67669,10703,27,98672,48664], 1)
    # assert r == 225735
