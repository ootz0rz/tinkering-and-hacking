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

# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
class Solution: 
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        goal = n - 1
        for i in range(n - 2, -1, -1):
            possibleEnd = i + nums[i]
            if possibleEnd >= goal:
                goal = i
        
        return goal == 0
        

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
        args=[[1,2,3,4,5,6,7], 3],
        expected=0
    )