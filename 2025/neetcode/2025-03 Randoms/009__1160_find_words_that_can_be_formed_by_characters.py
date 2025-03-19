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
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        
        d = defaultdict(int)
        for c in chars:
            d[c] += 1

        mem = defaultdict(int)
        for w in words:
            mem.clear()
            for c in w:
                mem[c] += 1

            # validate
            valid = True
            for c, num in mem.items():
                if d[c] < num:
                    valid = False
                    break
            
            if valid:
                ans += len(w)
        
        return ans

            


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.countCharacters

    check_solution_simple(
        sf,
        args=[["cat","bt","hat","tree"], "atach"],
        expected=6,
    )
