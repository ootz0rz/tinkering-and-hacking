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

# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/description/

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        pass
    
            
            

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.distinctNumbers

    check_solution_simple(
        sf,
        args=[[1,2,3,2,2,1,3], 3],
        expected=[3,2,2,2,3],
    )
