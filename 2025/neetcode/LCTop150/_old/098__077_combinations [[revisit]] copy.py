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

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        path = []
        def gen(start):
            nonlocal path, res

            if len(path) == k:
                res.append(path[:])
                return

            need = k - len(path) # how many more numbers we need for this path
            remain = n - start + 1 # how many digits we've consumed 
            avail = remain - need # the number of digits left to consume

            for d in range(start, start + avail + 1):
                path.append(d)
                gen(d + 1)
                path.pop()

        gen(1)

        #print(f"END: {res}")
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