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
        
        openStk = []
        unlockStk = []

        for idx in range(n):
            e = s[idx]
            isLocked = locked[idx] == LOCKED

            print(f"{idx}={e}, lock:{isLocked} -- open: {openStk}, unlocked: {unlockStk}")

            if not isLocked:
                unlockStk.append(idx)
            elif e == LEFT:
                openStk.append(idx)
            elif e == RIGHT:
                if len(openStk) > 0:
                    openStk.pop()
                elif len(unlockStk) > 0:
                    unlockStk.pop()
                else: 
                    return False
        
        print(f"=> open: {openStk}, unlock: {unlockStk}")
        while len(openStk) > 0 and len(unlockStk) > 0:
            if openStk[-1] <= unlockStk[-1]:
                openStk.pop()
                unlockStk.pop()

        if len(openStk) > 0:
            return False
        
        return len(unlockStk) % 2 == 0




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
