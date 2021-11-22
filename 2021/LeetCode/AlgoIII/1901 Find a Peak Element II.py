from typing import *

debug = False
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        # the idea is that we find the larges number with linear search in our pivot column
        # then check its left/right adjacent values...
        # if one of the left/right values is bigger, we then search that half of the grid instead

        pass


if __name__ == '__main__':
    debug = True
    s = Solution()
