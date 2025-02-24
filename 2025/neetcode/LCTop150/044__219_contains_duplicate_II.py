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

# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
'''
Idea: This is basically asking that, in a window of at most length k, do we have any dupes
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if n <= 1:
            return False
        
        i = 0
        j = 0
        seen = set()

        # expand our window
        while j < n and (j - i) < k:
            if nums[j] in seen:
                return True
            
            seen.add(nums[j])
            j += 1

        # slide our window along
        while i < j and j < n:
            if nums[j] in seen:
                return True
            
            seen.add(nums[j])
            seen.remove(nums[i])
            i += 1
            j += 1

        return False
        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.containsNearbyDuplicate

    check_solution_simple(  
        sf,
        args=[[1,2,3,1], 3],
        expected=True
    )