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

# https://neetcode.io/problems/minimum-stack
# https://leetcode.com/problems/min-stack/description/
class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if (len(self.prefix) == 0) or (val <= self.getMin()):
            self.prefix.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()

        if self.getMin() == popped:
            self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = MinStack()
    s.push(-2)
    s.push(-2)
    s.push(-3)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.getMin())