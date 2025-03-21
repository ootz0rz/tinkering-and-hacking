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

# https://leetcode.com/problems/before-and-after-puzzle/

SEP = " "
START = "start"
END = "end"
# n = len(phrases)
# P = len(max(phrases[]))
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        global SEP, START, END 

        d = {} # word: {start: [idx,...], end: [idx,...]}

        for idx, p in enumerate(phrases): # O(n)
            lidx = p.find(" ") # O(P)
            ridx = p.rfind(" ") # O(P)

            s = None
            e = None
            if lidx == -1:
                s = e = p
            else:
                s = p[:lidx]
                e = p[ridx + 1:]
            
            if not s in d:
                d[s] = {START: [], END: []}
            if not e in d:
                d[e] = {START: [], END: []}

            d[s][START].append(idx)
            d[e][END].append(idx)
        
        print(f"map: {d}")

        res = set()
        for word in d: # O(n)
            s = d[word][START]
            e = d[word][END]

            if len(s) == 0 or len(e) == 0:
                continue
            
            for sidx in e: # O(n)
                for eidx in s: # O(n)
                    if eidx == sidx:
                        continue

                    # NOTE a bit wasteful here, we generate duplicates sometimes
                    # Ex (sidx, edix) and then (edix, sidx)

                    newPhrase = phrases[sidx] + phrases[eidx][len(word):]
                    res.add(newPhrase)

        print(f"res: {res}")
        return sorted(list(res))



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.beforeAndAfterPuzzles

    check_solution_simple(
        sf,
        args=[["a","b","a"]], 
        expected=["a"],
    )

    check_solution_simple(
        sf,
        args=[["writing code","code rocks"]], 
        expected=["writing code rocks"],
    )

    check_solution_simple(
        sf,
        args=[["mission statement",
                  "a quick bite to eat",
                  "a chip off the old block",
                  "chocolate bar",
                  "mission impossible",
                  "a man on a mission",
                  "block party",
                  "eat my words",
                  "bar of soap"]], 
        expected=["a chip off the old block party",
         "a man on a mission impossible",
         "a man on a mission statement",
         "a quick bite to eat my words",
         "chocolate bar of soap"],
    )