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

# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150
CLOSING_PAIRS = {
    ")":"(",
    "]":"[",
    "}":"{",
}
#OPENING_PAIRS = set(['(','[','{'])
class Solution:
    def isValid(self, s: str) -> bool:
        global CLOSING_PAIRS

        stk = []

        for e in s:
            if e in CLOSING_PAIRS:
                if len(stk) > 0 and stk[-1] == CLOSING_PAIRS[e]:
                    stk.pop()
                    continue
                else:
                    return False

            stk.append(e)

        return len(stk) == 0

        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.longestConsecutive

    check_solution_simple(  
        sf,
        args=[[100,4,200,1,3,2]],
        expected=4
    )