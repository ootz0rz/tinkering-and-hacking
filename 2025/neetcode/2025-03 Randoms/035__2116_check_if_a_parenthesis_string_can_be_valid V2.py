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

# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

LEFT = "("
RIGHT = ")"
WILD = "*"
LOCKED = "1"
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        global LEFT, RIGHT, WILD, LOCKED
        n = len(s)

        if n % 2 != 0:
            return False
        
        numOpen = 0
        numClosed = 0
        numUnlocked = 0

        for idx in range(n):
            e = s[idx]
            isLocked = locked[idx] == LOCKED

            print(f"{idx}={e}, lock:{isLocked} -- open: {numOpen}, unlocked: {numUnlocked}")

            if not isLocked:
                numUnlocked += 1
            elif e == LEFT:
                numOpen += 1
            elif e == RIGHT:
                if numOpen > 0:
                    numOpen -= 1
                elif numUnlocked > 0:
                    numUnlocked -= 1
                else: 
                    return False
        
        print(f"=> open: {numOpen}, unlocked: {numUnlocked}")
        return numOpen <= numUnlocked




if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.canBeValid

    # check_solution_simple(
    #     sf,
    #     args=["((()(()()))()((()()))))()((()(()", "10111100100101001110100010001001"],
    #     expected=True,
    # )

    check_solution_simple(
        sf,
        args=["))()))", "010100"],
        expected=True,
    )
