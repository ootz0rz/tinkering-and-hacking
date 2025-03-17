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

# https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        m = {}
        def find(amt):
            nonlocal coins

            # at each step we can treat this like a BFS, checking every child
            # until we're at amt = 0
            if amt < 0:
                return -1 
            
            if amt == 0:
                return 0
            
            if not amt in m:
                count = float('inf')

                for c in coins:
                    res = find(amt - c)
                    if res != -1:
                        count = min(count, res + 1)
                        
                m[amt] = count if count != float('inf') else -1

            return m[amt]
                    
        return find(amount)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.coinChange

    check_solution_simple(
        sf,
        args=[[1,2,5], 11],
        expected=3,
    )
