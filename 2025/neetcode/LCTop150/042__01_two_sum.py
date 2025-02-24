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

# https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        i = 0
        while i < len(nums):
            e = nums[i]
            t = target - e

            if t in h:
                return (i, h[t])
            
            h[e] = i
            i += 1
        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.twoSum

    check_solution_as_sets(  
        sf,
        args=[[2,7,11,15], 9],
        expected=[0,1]
    )