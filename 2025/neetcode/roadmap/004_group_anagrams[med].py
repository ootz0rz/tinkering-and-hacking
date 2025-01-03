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

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            # gen freq list per element
            l = tuple(self.get_freq_list(s))

            if l in d:
                d[l].append(s)
            else:
                d[l] = [s]

        return list(d.values())
    
    def get_freq_list(self, s: str) -> List[int]:
        off = ord('a')

        l = [0]*26

        for i in s:
            io = ord(i) - off
            l[io] += 1
        
        return l

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    
    from TestHarness import *

    s = Solution()
    sf = s.groupAnagrams

    check_solution_as_frozensets(
        sf,
        args=[[""]],
        expected=[[""]],
    )

    check_solution_as_frozensets(
        sf,
        args=[["x"]],
        expected=[["x"]],
    )

    check_solution_as_frozensets(
        sf,
        args=[["act","pots","tops","cat","stop","hat"]],
        expected=[["hat"],["act", "cat"],["stop", "pots", "tops"]],
    )