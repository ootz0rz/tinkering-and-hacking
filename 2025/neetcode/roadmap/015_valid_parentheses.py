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

# https://neetcode.io/problems/validate-parentheses
# https://leetcode.com/problems/valid-parentheses/description/
_PAIRINGS_ = {
    ")" : "(",

    "}" : "{",

    "]" : "[",
}

class Solution:
    def isValid(self, s: str) -> bool:
        global _PAIRINGS_
        
        if len(s) == 0:
            return True
        
        if len(s) % 2 != 0:
            return False
        
        stack = []

        closers = set(_PAIRINGS_.keys())
        openers = set(_PAIRINGS_.values())
        for c in s:
            if c in openers:
                stack.append(c)
                continue
            
            if c in closers:
                if len(stack) > 0 and stack[-1] == _PAIRINGS_[c]:
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack) == 0


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isValid

    check_solution_simple(
        sf,
        args=[""],
        expected=True
    )

    check_solution_simple(
        sf,
        args=["["],
        expected=False
    )

    check_solution_simple(
        sf,
        args=["]"],
        expected=False
    )

    check_solution_simple(
        sf,
        args=["[]]"],
        expected=False
    )

    check_solution_simple(
        sf,
        args=["[]"],
        expected=True
    )

    check_solution_simple(
        sf,
        args=["([{}])"],
        expected=True
    )

    check_solution_simple(
        sf,
        args=["[(])"],
        expected=False
    )