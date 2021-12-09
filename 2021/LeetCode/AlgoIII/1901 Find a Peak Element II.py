# https://leetcode.com/problems/find-a-peak-element-ii/submissions/
from typing import *

debug = False


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # global debug

        # assuming mat[x] is xth column
        # mat[x][y] is yth value from xth column

        # the idea is that we find the larges number with linear search in our pivot column
        # then check its left/right adjacent values...
        # if one of the left/right values is bigger, we then search that half of the grid instead

        # if debug: print(f'\n------\nmat: {mat}')

        return self._findPeakGrid(mat, 0, len(mat))

    def _findPeakGrid(self, mat: List[List[int]], start_idx: int, end_idx: int) -> List[int]:
        # global debug

        def get_val(x: int, y: int) -> int:
            # takes care of returning -1 if x,y is outside mat's bounds
            if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[x]):
                return -1

            return mat[x][y]

        # if debug: print(f'===> start: {start_idx} end: {end_idx}')

        pivot = start_idx + ((end_idx - start_idx) // 2)

        # if debug: print(f'pivot: {pivot}')

        col = mat[pivot]

        # find largest value in column
        col_idx = 0
        largest_val = -1
        largest_idx = -1
        while col_idx < len(col):
            cur_val = get_val(pivot, col_idx)

            if cur_val >= largest_val:
                largest_val = cur_val
                largest_idx = col_idx

            col_idx = col_idx + 1

        # continue with largest idx and check adjacent
        col_idx = largest_idx
        left = get_val(pivot - 1, col_idx)
        right = get_val(pivot + 1, col_idx)

        # if we're bigger than both, we're done
        if largest_val > left and largest_val > right:
            # if debug: print(f'done! c:{largest_val} > l:{left} & r:{right} => {[pivot, col_idx]}')
            return [pivot, col_idx]

        if start_idx >= end_idx:
            # still no results? we done D:
            # if debug: print(f'searched everything, but no result...')
            return []

        # search in side that's biggest
        if right >= left:
            # search right
            # if debug: print(f'--> right: [{pivot}, {end_idx}]')
            return self._findPeakGrid(mat, pivot, end_idx)
        else:
            # search left
            # if debug: print(f'--> left: [{start_idx}, {pivot}]')
            return self._findPeakGrid(mat, start_idx, pivot)


if __name__ == '__main__':
    debug = True
    s = Solution()

    mat = [[1, 4], [3, 2]]
    r = s.findPeakGrid(mat)
    # print(f'mat: {mat} -> {r}')
    # assert r == [0, 1] or r == [1, 0]
    #
    # mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
    # r = s.findPeakGrid(mat)
    # print(f'mat: {mat} -> {r}')
    # assert r == [1, 1] or r == [2, 2]

    # mat = [[47, 30, 35, 8, 25], [6, 36, 19, 41, 40], [24, 37, 13, 46, 5], [3, 43, 15, 50, 19], [6, 15, 7, 25, 18]]
    # r = s.findPeakGrid(mat)
    # assert r == [0, 2]

    # mat = [[10,30,40,50,20],[1,3,2,500,4]]
    # r = s.findPeakGrid(mat)
