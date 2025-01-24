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

# https://neetcode.io/problems/minimum-window-with-characters

'''
Idea:

We calc freq of all letters in t.

Start a window at i,j from start to end of s

We remove i and j, respectively, if we can do so without going under our freq count. 
If we can no longer make any moves, and the freq count in our window is too small, 
then no match available.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s >= t or we can't match all chars
        if len(s) < len(t):
            return ""
        
        # gen freq maps
        matchesNeeded = 0
        tfreq = {}
        for i,e in enumerate(t):
            tfreq[e] = 1 + tfreq.get(e, 0)
            matchesNeeded += 1

        sfreq = {}
        for i,e in enumerate(s):
            if e in tfreq:
                sfreq[e] = 1 + sfreq.get(e, 0)
        
        i = 0
        j = len(s) - 1
        curMatches = 0
        while i <= j:
            ci = s[i]
            cj = s[j]

            # skip any letters we don't care about
            if not ci in tfreq:
                i = i + 1
                continue 

            if not cj in tfreq:
                j = j - 1
                continue

            didMove = False

            print(f"ci[{i}]: {ci} | cj[{j}]:{cj} -- tfreq:{tfreq} -- sfreq:{sfreq}")
            if sfreq[ci] - 1 >= tfreq.get(ci, 0):
                print(f"\t -> Remove ci[{i}]:{ci}")

                i = i + 1
                sfreq[ci] -= 1
                didMove = True

            if sfreq[cj] - 1 >= tfreq.get(cj, 0):
                print(f"\t -> Remove cj[{j}]:{cj}")

                j = j - 1
                sfreq[cj] -= 1
                didMove = True

            if not didMove:
                print(f"NO MOVE LEFT s[{i}:{j}] = {s[i:j+1]}")
                break

        doesMatch = True
        for k in tfreq.keys():
            if tfreq[k] != sfreq[k]:
                print(f"NO MATCH tfreq:{tfreq} vs sfreq:{sfreq}")
                return ""

        print(f"RETURN FINAL s[{i}:{j}] = {s[i:j+1]}")    
        return s[i:j+1]


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minWindow

    check_solution_simple(
        sf,
        args=["OUZODYXAZV", "XYZ"],
        expected="YXAZ"
    )

    check_solution_simple(
        sf,
        args=["xyz", "xyz"],
        expected="xyz"
    )

    check_solution_simple(
        sf,
        args=["x", "xy"],
        expected=""
    )
    