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

# https://leetcode.com/problems/lemonade-change/description/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        register = defaultdict(int)
        for b in bills:
            register[b] += 1

            if b == 20:
                c1 = (register[10] >= 1 and register[5] >= 1)
                c2 = (register[5] >= 3)

                if not (c1 or c2):
                    return False
                
                if c1:
                    register[10] -= 1
                    register[5] -= 1
                elif c2:
                    register[5] -= 3
            elif b == 10:
                if not register[5] >= 1:
                    return False
                
                register[5] -= 1
        
        return True

            

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