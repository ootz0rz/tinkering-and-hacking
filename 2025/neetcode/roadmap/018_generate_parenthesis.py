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

# https://neetcode.io/problems/generate-parentheses
# 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = []

        if n <= 0:
            return l

        self._gen(n, s="(", numopen=1, numclose=0, lst=l)

        return l

    def _gen(self, n, s, numopen, numclose, lst=[]):
        if (n == numopen) and (n == numclose):
            # print(f"BASE n:{n}, open:{numopen}, close:{numclose} => {s} -- {lst}")
            lst.append(s)
            return
        
        # invalid?
        if numclose > numopen:
            # print(f"\tINVALID BRANCH: {s}")
            return

        if numopen < n:
            # print(f"open:{numopen} < n:{n}")
            self._gen(n, s + "(", numopen=numopen + 1, numclose=numclose, lst=lst)

        if numclose < n:
            # print(f"close:{numclose} < n:{n}")
            self._gen(n, s + ")", numopen=numopen, numclose=numclose + 1, lst=lst)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.generateParenthesis

    check_solution_as_sets(
        sf,
        args=[1],
        expected=["()"]
    )

    check_solution_as_sets(
        sf,
        args=[2],
        expected=["(())", "()()"]
    )