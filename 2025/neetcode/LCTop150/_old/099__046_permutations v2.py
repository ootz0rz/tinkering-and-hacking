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

# https://leetcode.com/problems/permutations/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)

        path = []
        numset = set(nums)
        def gen():
            nonlocal res, numset

            if len(path) == n:
                res.append(path[:])
                return
            
            for d in nums:
                if d in numset:
                    path.append(d)
                    numset.remove(d)

                    gen()

                    numset.add(d)
                    path.pop()
        
        gen()
        return res



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.permute

    check_solution_simple(  
        sf,
        args=[[0, 1]],
        expected=[[0,1],[1,0]]
    )
