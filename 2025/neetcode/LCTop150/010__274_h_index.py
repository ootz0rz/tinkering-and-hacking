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

# https://en.wikipedia.org/wiki/H-index
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sort O(nlogn)
        s = sorted(citations)

        n = len(s)
        for idx, e in enumerate(s):
            ni = n - idx
            if e >= ni:
                return ni
        return 0
        

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