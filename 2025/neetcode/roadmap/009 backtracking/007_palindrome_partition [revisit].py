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

# https://neetcode.io/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partitions = []

        n = len(s)
        def find(left, right):
            nonlocal res

            if right >= n:
                if left == right:
                    res.append(partitions[:])
                    
                return
            
            if self._is_pali(s, left, right):
                partitions.append(s[left:right+1])
                find(right + 1, right + 1) # B
                partitions.pop()

            find(left, right + 1) # A

        find(0, 0)

        return res
    
    def _is_pali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            
            left = left + 1
            right = right - 1
        return True

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.partition

    check_solution_simple(  
        sf,
        args=["a"],
        expected=[["a"]]
    )

    check_solution_simple(  
        sf,
        args=["aab"],
        expected=[["a", "a", "b"], ["aa", "b"]]
    )