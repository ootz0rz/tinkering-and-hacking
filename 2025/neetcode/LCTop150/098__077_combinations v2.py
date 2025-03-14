from typing import List, Optional, Self, Set, Dict
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

# https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        path = []
        def gen(i, left):
            nonlocal res, path

            if len(path) == k:
                res.append(path[:])
                return 
            
            # determine the nodes at this level to visit
            for idx in range(i, n + 1):
                path.append(idx)

                gen(idx + 1, left - 1)

                path.pop()

        gen(1, k)
        return res
        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.combine

    check_solution_simple(  
        sf,
        args=[1, 1],
        expected=[[1]]
    )

    check_solution_simple(  
        sf,
        args=[4, 2],
        expected=[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    )