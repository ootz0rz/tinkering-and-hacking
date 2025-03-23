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

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

'''
Idea:

Sliding window starting at ends, and working towards making the items match each other
until the window meets in middle...? D:
'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        numOps = 0
        while i <= j:
            if nums[i] == nums[j]:
                i += 1
                j -= 1
            elif nums[i] < nums[j]:
                nums[i+1] += nums[i]
                numOps += 1
                i += 1
            else:
                nums[j-1] += nums[j]
                numOps +=1
                j -= 1
        
        return numOps
            

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.longestWPI

    check_solution_simple(
        sf,
        args=[[9,9,6,0,6,6,9]],
        expected=3,
    )

    check_solution_simple(
        sf,
        args=[[6,6,9]],
        expected=1,
    )