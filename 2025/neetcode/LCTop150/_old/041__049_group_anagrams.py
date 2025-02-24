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

# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = {}

        for i in range(len(s)):
            if not s[i] in m:
                m[s[i]] = 0

            if not t[i] in m:
                m[t[i]] = 0

            m[s[i]] += 1
            m[t[i]] -= 1
        
        for key in m:
            if m[key] != 0:
                return False

        return True
        
        

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