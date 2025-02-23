from typing import List, Optional, Self
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

# https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150
DIR = [
    # (row, col)
    (0, 1), # move right
    (1, 0), # move down
    (0, -1), # move left
    (-1, 0), # move up
]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def loop(leftBound, rightBound, topBound, bottomBound, res=[]):
            nonlocal matrix

            if leftBound >= rightBound or topBound >= bottomBound:
                return

            # go from left to right first
            col = leftBound
            row = topBound

            for col in range(leftBound, rightBound + 1):
                res.append(matrix[row][col])

            # go from top to bottom
            for row in range(topBound + 1, bottomBound + 1):
                res.append(matrix[row][col])

            if leftBound != rightBound:
                # go from right to left
                for col in range(rightBound - 1, leftBound - 1, -1):
                    res.append(matrix[bottomBound][col])

            if topBound != bottomBound:
                # go from bottom to top
                for row in range(bottomBound - 1, topBound, -1):
                    res.append(matrix[row][leftBound])

            # now check the inner matrix loop
            loop(leftBound + 1, rightBound - 1, topBound + 1, bottomBound - 1, res)

        r = []
        loop(0, len(matrix[0]), 0, len(matrix), r)

        return r


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.spiralOrder

    board = [[1,2,3],[4,5,6],[7,8,9]]

    check_solution_simple(  
        sf,
        args=[board],
        expected=[1,2,3,6,9,8,7,4,5]
    )

    check_solution_simple(  
        sf,
        args=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]]],
        expected=[1,2,3,4,8,12,11,10,9,5,6,7]
    )