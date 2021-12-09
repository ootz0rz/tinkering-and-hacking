# https://leetcode.com/problems/divide-chocolate/
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

from typing import *

debug = False

MAX_SWEET = 2**31-1

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        num_peeps = k + 1
        min_sweet = min(sweetness)
        max_sweet = sum(sweetness) // num_peeps

        if debug: print(f'\n-----\nsweetness: {sweetness}, num_peeps: {num_peeps}, range[{min_sweet}, {max_sweet}]')

        num_chunks, smallest = _maximizeSweetness(sweetness, num_peeps, min_sweet, max_sweet)
        return smallest


def _maximizeSweetness(sweetness: List[int], num_peeps: int, min_sweet: int, max_sweet: int) -> List[int]:
    global debug

    if min_sweet > max_sweet:
        return [-1, -1]

    sweetness_target = min_sweet + (max_sweet - min_sweet) // 2

    if debug: print(f'\tnum_peeps: {num_peeps} range[{min_sweet}:{max_sweet}] target: {sweetness_target}')

    num_chunks, smallest_chunk = _get_chunks(sweetness, sweetness_target)

    if debug: print(f'\t\tchunks: {num_chunks}, smallest: {smallest_chunk}, target: {sweetness_target}')

    if num_chunks < num_peeps:
        if min_sweet == max_sweet:
            if debug: print(f'\t\t --> left end of line: [num: {num_chunks}, smallest: {smallest_chunk}]')
            return [num_chunks, smallest_chunk]

        # we failed to get a large enough value
        if debug: print(f'\t\t --> left range: [{min_sweet}:{sweetness_target-1}]')
        left_num, left_val = _maximizeSweetness(sweetness, num_peeps, min_sweet, sweetness_target-1)

        if left_num >= num_peeps:
            if debug: print(f'\t\t --> left valid: [num: {left_num}, smallest: {left_val}]')
            return [left_num, left_val]
        else:
            if debug: print(f'\t\t --> left invalid: [num: {num_chunks}, smallest: {smallest_chunk}]')
            return [num_chunks, smallest_chunk]

    if num_chunks >= num_peeps:
        # we have at least as many chunks as peeps

        # we need to check the right hand side and see if there's another better value
        if debug: print(f'\t\t --> right range: [{sweetness_target+1}:{max_sweet}]')
        right_num, right_val = _maximizeSweetness(sweetness, num_peeps, sweetness_target+1, max_sweet)

        if right_num >= num_peeps:
            if debug: print(f'\t\t --> right valid: [num: {right_num}, smallest: {right_val}]')
            return [right_num, right_val]
        else:
            if debug: print(f'\t\t --> right invalid: [num: {num_chunks}, smallest: {smallest_chunk}]')
            return [num_chunks, smallest_chunk]

def _get_chunks(sweetness: List[int], sweetness_target: int) -> List[int]:
    """
    return [num_chunks, smallest_val]
    """
    idx = 0

    num_chunks = 0
    cur_chunk_val = 0

    smallest_chunk = MAX_SWEET
    while idx < len(sweetness):
        cur_sweet = sweetness[idx]

        cur_chunk_val = cur_chunk_val + cur_sweet
        if cur_chunk_val >= sweetness_target:

            if cur_chunk_val <= smallest_chunk:
                smallest_chunk = cur_chunk_val

            num_chunks = num_chunks + 1
            cur_chunk_val = 0

        idx = idx + 1

    return [num_chunks, smallest_chunk]

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

    r = s.maximizeSweetness([87506,32090,9852,96263,52415,67669,10703,27,98672,48664], 1)
    assert r == 225735

    # r = _get_chunks([1, 2, 2, 1, 2, 2, 1, 2, 2], 6)
    # print(f'num_peeps={2+1} num: {r[0]} smallest: {r[1]}')
    # r = s.maximizeSweetness([1, 2, 2, 1, 2, 2, 1, 2, 2], 2)
    # print(f'{r}')
