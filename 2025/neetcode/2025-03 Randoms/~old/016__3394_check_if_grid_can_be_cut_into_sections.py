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

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/

'''
Idea:

Check intervals horizontal, and then check vertical, to see if any set works
'''
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def process(si, ei): # O(nlogn)
            nonlocal n, rectangles

            rectangles.sort(key=lambda x: x[si]) # O(nlogn)

            print(f"PROCESS {si}, {ei} => {rectangles}")

            intervals = [] # O(3)
            for e in rectangles: # O(n)
                cs = e[si]
                ce = e[ei]

                print(f"\t Cur Interval: <{intervals}> vs next <{cs},{ce}>")

                if len(intervals) == 0 or intervals[-1][1] <= cs:
                    intervals.append([cs, ce])
                else:
                    intervals[-1][1] = max(intervals[-1][1], ce)

                print(f"\t\t => intervals: {intervals}")
                if len(intervals) >= 3:
                    # we have enough to split so can just end here, rest can be put into a single bucket if need be
                    return True
                
            return len(intervals) >= 3

        return process(0, 2) or process(1, 3) # O(2n)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.checkValidCuts

    check_solution_simple(
        sf,
        args=[5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]],
        expected=True,
    )

