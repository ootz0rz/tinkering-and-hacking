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

# https://neetcode.io/problems/is-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            # skip non-alpha
            while not s[i].isalnum() and i < j:
                i = i + 1

            while not s[j].isalnum() and i < j:
                j = j - 1

            if s[i].lower() != s[j].lower():
                return False
        
            i = i + 1
            j = j - 1
            
        return True
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isPalindrome

    check_solution_simple(
        sf,
        args=["Was it a car or a cat I saw?"],
        expected=True
    )

    check_solution_simple(
        sf,
        args=["tab a cat"],
        expected=False
    )