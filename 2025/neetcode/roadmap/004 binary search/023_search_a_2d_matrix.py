from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://neetcode.io/problems/binary-search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])

        left = 0
        right = numRows * numCols - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            # we use numCols for both here, since the row number is determined by how many
            # columns there are in this case
            #
            # but we used numRows * numCols - 1, above, to determine how many rows of columns
            # that we have total
            curRow = mid // numCols
            curCol = mid % numCols

            e = matrix[curRow][curCol]
            if e == target:
                return True
            
            if e > target:
                # discard right
                right = mid - 1
            else:
                # discard left
                left = mid + 1
        
        return False
            
            



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.searchMatrix

    check_solution_simple(
        sf,
        args=[[[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10],
        expected=True
    )

    check_solution_simple(
        sf,
        args=[[[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15],
        expected=False
    )

    
