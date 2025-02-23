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

# https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150
'''
Idea:

Track the rows and cols with a 0 in them on first pass

Then 0 them out on 2nd pass

We can track this in matrix itself
'''
_MATCHER = 0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        global _MATCHER, _DIR

        nodes = set()
        n = len(matrix)
        m = len(matrix[0])

        # mark what should be zeroed out
        firstRow = False 
        firstCol = False

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell != _MATCHER:
                    continue

                if i == 0:
                    firstRow = True

                if j == 0:
                    firstCol = True
            
                matrix[i][0] = _MATCHER
                matrix[0][j] = _MATCHER
        
        # set zeroes except on first row and col
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == _MATCHER or matrix[0][j] == _MATCHER:
                    matrix[i][j] = _MATCHER

        # set zeroes on first row/col if needed
        if firstRow:
            for j in range(0, m):
                matrix[0][j] = _MATCHER
        
        if firstCol:
            for i in range(0, n):
                matrix[i][0] = _MATCHER
        
        return matrix


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.setZeroes

    check_solution_simple(  
        sf,
        args=[[[1,1,1],[1,0,1],[1,1,1]]],
        expected=[[1,0,1],[0,0,0],[1,0,1]]
    )

    check_solution_simple(  
        sf,
        args=[[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]],
        expected=[[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    )
