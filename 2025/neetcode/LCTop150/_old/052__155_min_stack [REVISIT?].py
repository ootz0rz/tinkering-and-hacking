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

# https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150
class MinStack:

    def __init__(self):
        self.s = [] # main stack
        self.min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        
        if len(self.min) == 0 or val <= self.getMin():
            self.min.append(val)

    def pop(self) -> None:
        p = self.s.pop()

        if p == self.getMin():
            self.min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    check_solution_simple(  
        s.getMin,
        args=[],
        expected=-3
    )
    s.pop()
    check_solution_simple(  
        s.top,
        args=[],
        expected=0
    )
    check_solution_simple(  
        s.getMin,
        args=[],
        expected=-2
    )