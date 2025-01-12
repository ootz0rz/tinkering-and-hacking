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

# https://neetcode.io/problems/buy-and-sell-crypto

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) - 1

        if len(prices) <= 1:
            return 0

        i = 0
        j = 1
        
        maxProfit = 0

        while (i < j) and (j <= n):
            pj = prices[j]
            pi = prices[i]

            curProfit = pj - pi
            maxProfit = max(maxProfit, curProfit)

            if pj < pi:
                # found a new smaller purchase price
                i = j
            
            # keep on sliding
            j = j + 1

        return maxProfit


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.maxProfit

    check_solution_simple(
        sf,
        args=[[10,1,5,6,7,1]],
        expected=6
    )

    check_solution_simple(
        sf,
        args=[[10,8,7,5,2]],
        expected=0
    )


    