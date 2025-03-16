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

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        # we can treat this all as an extended list, just need to calculate the values
        L = 0
        R = n * m - 1

        while L <= R:
            mid = L + ((R-L) // 2)

            x = mid // m
            y = mid % m

            # print(f"target: {target}, {mid} => {x},{y} => {matrix[x]}")

            if matrix[x][y] == target:
                return True

            if matrix[x][y] > target:
                R = mid - 1
            else:
                L = mid + 1
        
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
        args=[[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3],
        expected=True,
    )