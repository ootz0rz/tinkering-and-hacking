from typing import List,Optional
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
import sys

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-interview-150
# https://leetcode.com/problems/longest-increasing-subsequence/editorial/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        m = {}
        def find(idx):
            nonlocal nums, m 

            if idx >= len(nums):
                return 0
            
            

        return find(0)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.lengthOfLIS

    check_solution_simple(
        sf,
        args=[[10,9,2,5,3,7,101,18]],
        expected=4,
    )
