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

        m = {}
        def canSegment(i, j):
            nonlocal s, wordDict, m, words

            if i >= j:
                return False

            coord = (i,j)
            if coord in m:
                return m[coord]

            if s[i:j] in words:
                m[coord] = True
                return True 

            left = False
            right = False
            for pivot in range(i+1, j):

                left = canSegment(i, pivot)
                right = canSegment(pivot, j)

                if left and right:
                    break
            
            m[coord] = left and right
            return left and right

        return canSegment(0, len(s))

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
