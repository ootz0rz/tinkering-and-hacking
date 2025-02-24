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

# https://leetcode.com/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force O(n^3)
        
        max_seq = 0
        for n in nums:

            cur_seq = 1
            nn = n + 1
            while nn in nums:
                nn += 1
                cur_seq += 1

            max_seq = max(max_seq, cur_seq)
        
        return max_seq
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.longestConsecutive

    check_solution_simple(  
        sf,
        args=[[100,4,200,1,3,2]],
        expected=4
    )