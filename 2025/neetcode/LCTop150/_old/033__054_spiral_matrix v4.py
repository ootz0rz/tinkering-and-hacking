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
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = []

        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)


        while left < right and top < bottom:
            #print(f"TOP OF LOOP: {r}")

            # get all elements in top row, left to right
            #print()
            #print(f" -> LEFT TO RIGHT: col in {list(range(left, right))}")
            for col in range(left, right):
                #print(f"\t 0 -> {top},{col} = {matrix[top][col]}")
                r.append(matrix[top][col])
            top += 1
                

            # get all elements in right col, top to bottom
            # NOTE: skip top right
            #print()
            #print(f" -> TOP TO BOT: row in {list(range(top + 1, bottom))}")
            for row in range(top, bottom):
                #print(f"\t 1 -> {row},{right - 1} = {matrix[row][right - 1]}")
                r.append(matrix[row][right - 1])
            right -= 1
            
            # check bounds
            if left >= right or top >= bottom:
                break

            # get all elements in bottom row, right to left
            # NOTE: skip bottom right
            #print()
            #print(f" -> RIGHT TO LEFT: col in {list(range(right - 1, left - 1, -1))}")
            for col in range(right - 1, left - 1, -1):
                #print(f"\t 2 -> {bottom - 1},{col} = {matrix[bottom - 1][col]}")
                r.append(matrix[bottom - 1][col]) 
            bottom -= 1

            # get all elements in first column, bottom to top
            # NOTE: skip bottom left and top left
            #print()
            #print(f" -> BOT TO TOP: row in {range(bottom - 1, top+1, -1)}")
            for row in range(bottom - 1, top - 1, -1):
                #print(f"\t 3 -> {row},{left} = {matrix[row][left]}")
                r.append(matrix[row][left])
            left += 1
        

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