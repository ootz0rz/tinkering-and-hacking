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

# https://neetcode.io/problems/permutation-string

'''
Idea:

Track freq of s1, sliding window and track its freq from s2... if freq_s2 == freq_s1, then done.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0

        if len(s1) > len(s2):
            return False

        # Note, s1freq size is bounded by a-z => 26... O(26) => O(1)
        # just using a hash for convenience to avoid ORD calcs to find index
        s1freq = {}
        for s in s1:
            s1freq[s] = 1 + s1freq.get(s, 0)

        curMatches = 0 # number of letters we've matched frequencies of
        totalMatchesNeeded = len(s1freq)

        s2freq = {} # Also bounded O(26)
        while i <= j and j < len(s2):
            cj = s2[j]

            # if we encounter an unwanted letter, we know it's not gonna be part of our substring, so just skip the mess
            if not cj in s1freq:
                i = j
                j = j + 1
                curMatches = 0
                s2freq.clear()
                continue

            s2freq[cj] = 1 + s2freq.get(cj, 0)

            if s2freq[cj] == s1freq[cj]:
                curMatches += 1

            elif s2freq[cj] == s1freq[cj] + 1:
                while s2freq[cj] > s1freq[cj]:
                    ci = s2[i]

                    if ci in s2freq and s2freq[ci] == s1freq[ci]:
                        curMatches -= 1
                    
                    s2freq[ci] = max(0, s2freq.get(ci, 0) - 1)

                    i = i + 1

            if curMatches == totalMatchesNeeded:
                return True

            j = j + 1

        return False


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.checkInclusion

    check_solution_simple(
        sf,
        args=["abc", "lecabee"],
        expected=True
    )

    check_solution_simple(
        sf,
        args=["abc", "lecaabee"],
        expected=False
    )

    check_solution_simple(
        sf,
        args=["adc", "dcda"],
        expected=True
    )
    