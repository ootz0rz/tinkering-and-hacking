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

# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        # try to do this by checking each word first, instead of segmenting through entire word?
        # Uses O(N) memory instead of O(N^2) like before

        m = {}
        def canSegment(idx):
            nonlocal s, wordDict, m, words

            if idx >= len(s):
                return True

            if idx in m:
                return m[idx]
            
            #print(f"Can Segment: {idx}")

            for w in words:
                wl = len(w)

                #print(f"\t check {w} == s[{idx}:{idx+wl}]={s[idx:idx+wl]}")

                if s[idx:idx+wl] == w and canSegment(idx + wl):
                    m[idx] = True
                    return True
            
            m[idx] = False
            return False

        r = canSegment(0)
        #import pprint; pprint.pprint(m)
        return r

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.wordBreak

    check_solution_simple(
        sf,
        args=["leetcode", ["leet","code"]],
        expected=True,
    )
