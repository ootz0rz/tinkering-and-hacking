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

# https://leetcode.com/problems/combination-sum/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # Much easier if the list is sorted, and in reverse order
        candidates.sort() # O(nlogn)
        candidates.reverse()

        path = []
        def gen(sum):
            nonlocal res, path

            # print(f"GEN sum:{sum} == t:{target}?")
            
            if sum == target:
                res.append(path[:]) # must copy, O(n)
                return 
            
            for d in candidates:
                if d > target:
                    continue # skip nums too large
                
                path.append(d)

                gen(sum + d)

                path.pop()
                    
        gen(0)
        return res 


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.combinationSum

    check_solution_simple(  
        sf,
        args=[[2], 1],
        expected=[]
    )

    check_solution_simple(  
        sf,
        args=[[1,2], 1],
        expected=[[1]]
    )