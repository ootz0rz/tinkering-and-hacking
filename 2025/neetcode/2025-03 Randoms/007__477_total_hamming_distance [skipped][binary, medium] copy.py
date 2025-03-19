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

# https://leetcode.com/problems/total-hamming-distance/

'''
Idea:

Each num is 32bit long. n = len(nums)

We'll loop through each bit, and then each number. Count how many
numbers have that bit set to 1. If there are A 1s, then there are n-A 0s

So the dist by this bit is A(n-A) = An - A**2
'''
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)

        for 
        pass

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.wordBreak

    check_solution_as_frozensets(
        sf,
        args=["catsanddog", ["cat","cats","and","sand","dog"]],
        expected=["cats and dog","cat sand dog"],
    )

    check_solution_as_frozensets(
        sf,
        args=["pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]],
        expected=["pine apple pen apple","pineapple pen apple","pine applepen apple"],
    )

    check_solution_as_frozensets(
        sf,
        args=["catsandog", ["cats","dog","sand","and","cat"]],
        expected=[],
    )