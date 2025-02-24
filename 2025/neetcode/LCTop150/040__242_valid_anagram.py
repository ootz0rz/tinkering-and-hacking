from typing import List, Optional, Self
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

# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        smap = defaultdict(list)
        oa = ord('a')

        for s in strs:
            # count 
            d = [0] * 26
            for e in s:
                d[ord(e) - oa] += 1

            smap[tuple(d)].append(s)
        
        r = []
        for key in smap:
            rc = []
            for e in smap[key]:
                rc.append(e)
            r.append(rc)
        
        return r


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.isAnagram

    check_solution_simple(  
        sf,
        args=["anagram", "nagaram"],
        expected=True
    )