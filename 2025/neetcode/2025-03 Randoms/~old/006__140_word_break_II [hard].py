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

# https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ans = []
        path = []

        def search(curs: str):
            if len(curs) == 0:
                return
            
            for word in wordDict:
                if not curs.startswith(word):
                    # invalid branch
                    continue
                
                path.append(word)

                if len(curs) == len(word):
                    # we reached an end-point
                    ans.append(" ".join(path))
                else:
                    # more to explore
                    search(curs[len(word):])

                path.pop()
        
        search(s)
        return ans

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.wordBreak

    check_solution_as_frozensets(
        sf,
        args=["catsanddog", ["cat","cats","and","sand","dog"]],
        expected=["cats and dog","cat sand dog"],
    )

    check_solution_as_frozensets(
        sf,
        args=["pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]],
        expected=["pine apple pen apple","pineapple pen apple","pine applepen apple"],
    )

    check_solution_as_frozensets(
        sf,
        args=["catsandog", ["cats","dog","sand","and","cat"]],
        expected=[],
    )