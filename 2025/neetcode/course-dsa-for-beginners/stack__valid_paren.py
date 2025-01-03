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

pairings = {
    ')' : '(',

    '}' : '{',

    ']' : '[',
}

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []

        for e in s:
            if not (e in pairings):
                stack.append(e)
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] == pairings[e]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isValid
