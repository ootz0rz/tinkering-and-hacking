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
import sys

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        costs.sort()

        mem = {}
        def search(idx, c1, c2):
            nonlocal mem, n, costs

            print(f"Search idx:{idx}, c1:{c1}, c2:{c2}")

            if (c1 < 0 and c2 < 0) or (idx >= len(costs)):
                print(f"\t => idx:{idx}, c1:{c1}, c2:{c2} => OUT OF BOUNDS")
                return 0 #float('inf')
            
            if not idx in mem:
                mc = 0
                if costs[idx][0] > costs[idx][1]:
                    mc = costs[idx][1]
                    c2 -= 1
                else:
                    mc = costs[idx][0]
                    c1 -= 1

                mem[idx] = mc + search(idx + 1, c1, c2)
                print(f"\t => idx:{idx}, c1:{c1}, c2:{c2} => GEN: {mem[idx]}")
            else:
                print(f"\t => idx:{idx}, c1:{c1}, c2:{c2} => RETURN: {mem[idx]}")

            return mem[idx]

        return search(0, n, n)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.twoCitySchedCost

    check_solution_simple(
        sf,
        args=[[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]],
        expected=1859,
    )
