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
        
        ns = []
        for idx in range(n):
            isLocked = locked[idx] == LOCKED

            if not isLocked:
                ns.append(WILD)
            else:
                ns.append(s[idx])
        
        s = "".join(ns)

        print(f"s: {s}")
        
        stk = []
        for idx in range(n):
            e = s[idx]

            print(f"{idx}={e}, stk:{stk} of {s}")

            if e == RIGHT or e == WILD:
                if len(stk) > 0 and (stk[-1] == LEFT or stk[-1] == WILD):
                    stk.pop()
                    continue
                elif e == WILD:
                    stk.append(e)
                    continue
                else:
                    return False

            stk.append(e)
        
        print(f"-> {stk} => {(len(stk) == 0)}")
        return len(stk) == 0

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
