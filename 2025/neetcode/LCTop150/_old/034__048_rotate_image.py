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
    def rotate(self, matrix: List[List[int]]) -> None:        
        left = 0
        right = len(matrix)
        top = 0
        bottom = right

        while left < right and top < bottom:
            # NOTE that we always expect i to be 0-based, we only care how many elements are in this row of submatrix
            #      we do not want i to be from left to right, instead we want to calc later below left+i to figure out
            #      what our current column is, for example
            for i in range(right - left - 1):
                t = matrix[top][left + i]
                #print(f"i: {i} t TOP:{t}")

                # replace TOP with LEFT
                #print(f"\t top[{top}][{left + i}]:{matrix[top][left + i]} = left[{bottom - 1 - i}][{left}]:{matrix[bottom - 1 - i][left]}")
                matrix[top][left + i] = matrix[bottom - 1 - i][left]

                # replace LEFT with BOT
                #print(f"\t left[{bottom - 1 - i}][{left}]:{matrix[bottom - 1 - i][left]} = bot[{bottom - 1}][{right - 1 - i}]:{matrix[bottom - 1][right - 1 - i]}")
                matrix[bottom - 1 - i][left] = matrix[bottom - 1][right - 1 - i]

                # replace BOT with RIGHT
                #print(f"\t bot[{bottom - 1}][{right - 1 - i}]:{matrix[bottom - 1][right - 1 - i]} = right[{top + i}][{right - 1}]:{matrix[top + i][right - 1]}")
                matrix[bottom - 1][right - 1 - i] = matrix[top + i][right - 1]

                # replace RIGHT with TOP
                #print(f"\t right[{top + i}][{right - 1}]:{matrix[top + i][right - 1]} = top[{top}][{left + i}]:{t}")
                matrix[top + i][right - 1] = t

            #print(matrix)

            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.rotate

    check_solution_simple(  
        sf,
        args=[[[1,2,3],[4,5,6],[7,8,9]]],
        expected=[[7,4,1],[8,5,2],[9,6,3]]
    )

    check_solution_simple(  
        sf,
        args=[[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]],
        expected=[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    )
