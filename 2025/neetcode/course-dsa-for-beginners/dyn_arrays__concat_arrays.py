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

# https://leetcode.com/problems/concatenation-of-array/description/
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        L = len(nums)

        arr = [0] * (L*2)
        
        i = 0
        j = L

        while i < L:
            arr[i] = arr[j] = nums[i]
            i = i + 1
            j = j + 1
        
        return arr

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.getConcatenation
