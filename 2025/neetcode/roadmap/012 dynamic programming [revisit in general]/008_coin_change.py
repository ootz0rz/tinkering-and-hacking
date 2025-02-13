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

# https://neetcode.io/problems/decode-ways

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [amount + 1] * (amount + 1)
        mem[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if (a - c) >= 0:
                    mem[a] = min(mem[a], 1 + mem[a - c])
        
        if mem[amount] != (amount+1):
            return mem[amount]
        
        # O(amount * n)
        return -1

        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.coinChange

    check_solution_simple(  
        sf,
        args=[[1], 0],
        expected=0
    )

    check_solution_simple(  
        sf,
        args=[[1], 5],
        expected=5
    )

    check_solution_simple(  
        sf,
        args=[[5], 5],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=[[1,5], 10],
        expected=2
    )

    check_solution_simple(  
        sf,
        args=[[1, 5], 12],
        expected=4
    )