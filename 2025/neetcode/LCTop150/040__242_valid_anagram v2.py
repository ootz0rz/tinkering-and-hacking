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
_PRIME_MAP = {
    'a': 2, 
    'b': 3, 
    'c': 5, 
    'd': 7, 
    'e': 11, 
    'f': 13,
    'g': 17,
    'h': 19,
    'i': 23,
    'j': 29,
    'k': 31,
    'l': 37,
    'm': 41,
    'n': 43,
    'o': 47,
    'p': 53,
    'q': 59,
    'r': 61,
    's': 67, 
    't': 71,
    'u': 73,
    'v': 79,
    'w': 83,
    'x': 89,
    'y': 97,
    'z': 101
}
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # NOTE using primes here only works with small vals
        #      
        #      this works fine in python because ints can go really large
        #      but might overflow elsewhere
        global _PRIME_MAP
        smap = defaultdict(list)

        for s in strs:
            # count 
            p = 1
            for e in s:
                p *= _PRIME_MAP[e]

            smap[p].append(s)
        
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