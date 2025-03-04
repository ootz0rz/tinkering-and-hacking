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

# https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        global ops 
        proc = []

        for t in tokens:
            if t == "+":
                proc.append(proc.pop() + proc.pop())
            elif t == "-":
                right = proc.pop()
                left = proc.pop()
                proc.append(left - right)
            elif t == "*":
                proc.append(proc.pop() * proc.pop())
            elif t == "/":
                right = proc.pop()
                left = proc.pop()
                proc.append(int(left / right)) # we do left/right and then just convert to int, truncating remainder
            else:
                proc.append(int(t))
        
        return proc[0]

        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.evalRPN

    check_solution_simple(  
        sf,
        args=[["1", "1", "+"]],
        expected=2
    )
