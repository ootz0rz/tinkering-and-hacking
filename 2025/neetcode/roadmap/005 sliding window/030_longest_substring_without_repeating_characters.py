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

# https://neetcode.io/problems/longest-substring-without-duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        i = 0
        j = 1

        maxLen = 1
        uniques = set([s[0]])
        while j <= n - 1:

            # print(f"Cur Window: {i}:{j} => s[i:j]<{s[i:j]}> -- uniq:{uniques}")

            while s[j] in uniques and i < j:
                # print(f"\t\tRemove: s[i:{i}]:{s[i]}")
                uniques.remove(s[i])
                i = i + 1

            uniques.add(s[j])
            maxLen = max(maxLen, len(uniques))

            j = j + 1

            # print(f"\tNext Window: {i}:{j} => s[i:j]<{s[i:j]}> -- uniq:{uniques}")
        
        return maxLen
            


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.lengthOfLongestSubstring

    check_solution_simple(
        sf,
        args=["pwwkew"],
        expected=3
    )

    check_solution_simple(
        sf,
        args=["zxyzxyz"],
        expected=3
    )

    check_solution_simple(
        sf,
        args=["xxxx"],
        expected=1
    )


    