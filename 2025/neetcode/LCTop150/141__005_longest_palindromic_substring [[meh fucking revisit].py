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

# https://leetcode.com/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-interview-150

## DP COURSES https://leetcode.com/discuss/post/5659029/ultimate-dynamic-programming-series-on-l-vpys/

# 2ptr easy enough, but about about 2DP?
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def expand(i, j):
            l = 0
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                l = j - i - 1
            
            return l
        
        maxLen = 0
        start = 0
        end = 0
        for i in range(n):
            evenLen = expand(i-1, i+1)
            oddLen = expand(i, i + 1)

            curMax = max(evenLen, oddLen)

            if curMax > maxLen:
                start = i - ((curMax - 1)//2)
                end = i + (curMax//2)

                maxLen = curMax
        
        # print(f"{start},{end}")
        return s[start:end+1]
            


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.longestPalindrome

    check_solution_simple(
        sf,
        args=["babad"],
        expected="bab",
    )

    check_solution_simple(
        sf,
        args=["cbbd"],
        expected="bb",
    )