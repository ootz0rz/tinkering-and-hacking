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

# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
'''

'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maxVol = 0
        while i < j:
            hi = heights[i]
            hj = heights[j]

            maxVol = max(maxVol, (j - i) * min(hi, hj)) 
            
            # replace the min value and keep searching
            if hi < hj:
                i += 1
            else:
                j -= 1
        
        return maxVol

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.twoSum

    check_solution_simple(  
        sf,
        args=[[2,7,11,15], 9],
        expected=[1, 2]
    )
