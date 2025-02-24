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

# https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and not n in seen:
            seen.add(n)

            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            n = s
        
        return n == 1
        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.isHappy

    check_solution_simple(  
        sf,
        args=[2],
        expected=False
    )