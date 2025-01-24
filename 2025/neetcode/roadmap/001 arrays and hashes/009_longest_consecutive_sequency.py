from typing import List
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

'''
https://neetcode.io/problems/longest-consecutive-sequence
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set(nums)
        longest = 0

        for e in exists:
            if (e - 1) in exists:
                # skip since we're not the potential start of a sequence
                continue
            
            # check rest of sequence
            l = 1
            while (e + l) in exists:
                l = l + 1
            
            longest = max(l, longest)

        return longest



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.longestConsecutive

    check_solution_simple(
        sf,
        args=[[2,20,4,10,3,4,5]],
        expected=4
    )

    check_solution_simple(
        sf,
        args=[[0,3,2,5,4,6,1,1]],
        expected=7
    )