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

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        numWays = 0

        while total >= 0:
            numWays += 1 + (total // cost2)
            total -= cost1 
        
        return numWays
        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.waysToBuyPensPencils

    # check_solution_simple(
    #     sf,
    #     args=["((()(()()))()((()()))))()((()(()", "10111100100101001110100010001001"],
    #     expected=True,
    # )

    check_solution_simple(
        sf,
        args=[20, 10, 5],
        expected=9,
    )
