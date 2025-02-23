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

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxProf = 0
        while (l < r) and r < len(prices):
            el = prices[l]
            er = prices[r]

            curProfit = er - el
            maxProf = max(maxProf, curProfit)

            if er < el:
                l = r 
            
            r = r + 1

        return maxProf

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