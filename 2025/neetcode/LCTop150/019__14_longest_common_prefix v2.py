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

# https://leetcode.com/problems/longest-common-prefix/submissions/1546903852/?envType=study-plan-v2&envId=top-interview-150
'''
Idea:

Take first word as prefix, compare with 2nd word... if we don't match, then start to remove a letter
from the end of our prefix one at a time until we have a match

If we end up having a prefix of 0 length, return empty

Otherwise, check again with all the rest of the items
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        for s in strs:

            while not s.startswith(prefix):
                prefix = prefix[:-1]

            if len(prefix) == 0:
                return ""

        return prefix



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.longestCommonPrefix

    check_solution_simple(  
        sf,
        args=[["flower","flow","flight"]],
        expected="fl"
    )

    check_solution_simple(  
        sf,
        args=[["dog","racecar","car"]],
        expected=""
    )

    check_solution_simple(  
        sf,
        args=[["ab", "a"]],
        expected="a"
    )

    check_solution_simple(  
        sf,
        args=[["ab", "ab"]],
        expected="ab"
    )