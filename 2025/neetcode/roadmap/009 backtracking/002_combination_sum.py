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

# https://neetcode.io/problems/combination-target-sum

class Solution:
    # kinda works, but returns dupes... i.e all permutations not combinations
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def find(sum, path, idx):
            nonlocal res

            for i,n in enumerate(nums[idx:]):

                if n > target:
                    continue
                
                sn = sum + n 

                if sn == target:
                    res.append(path + [n])
                    
                elif sn < target:
                    find(sn, path + [n], i)
        
        find(0, [], 0)

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

    check_solution_as_frozensets(
        sf,
        args=[[3], 5],
        expected=[]
    )

    check_solution_as_frozensets(
        sf,
        args=[[2,5,6,9], 9],
        expected=[[2,2,5], [9]]
    )


