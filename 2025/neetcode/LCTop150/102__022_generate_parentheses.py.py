from typing import List, Optional, Self, Set, Dict
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

# https://leetcode.com/problems/combination-sum/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        path = []
        def gen(o, c):
            nonlocal res, path # important to mark as nonlocal or else we end up making copies within!!!

            if c < o:
                return # invalid

            if o == 0 and c == 0:
                res.append("".join(path))
                return

            if o > 0:
                path.append("(")
                gen(o - 1, c)
                path.pop()

            if c > 0:
                path.append(")")
                gen(o, c - 1)
                path.pop()

        gen(n, n)
        return res 


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.generateParenthesis

    check_solution_simple(  
        sf,
        args=[1],
        expected=["()"]
    )

    check_solution_as_tuplesets(  
        sf,
        args=[2],
        expected=["()()", "(())"]
    )

    check_solution_as_tuplesets(  
        sf,
        args=[3],
        expected=["((()))","(()())","(())()","()(())","()()()"]
    )