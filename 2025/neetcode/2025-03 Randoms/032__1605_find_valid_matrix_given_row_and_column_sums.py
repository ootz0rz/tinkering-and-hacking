from typing import List,Optional
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

# https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum) 
        m = len(colSum) 

        outM = [[0] * m for _ in range(n)]

        curRow = [0] * n
        curCol = [0] * m
        
        for x, row in enumerate(outM):
            for y, cell in enumerate(row):

                outM[x][y] = min(
                    rowSum[x] - curRow[x],
                    colSum[y] - curCol[y]
                )

                curRow[x] += outM[x][y]
                curCol[y] += outM[x][y]
        
        return outM
                


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.repairCars

    check_solution_simple(
        sf,
        args=[[4,2,3,1], 10],
        expected=16,
    )
