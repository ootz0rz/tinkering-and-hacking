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

# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        pidx = 0
        n = len(strs)
        while pidx >= 0 and pidx <= len(strs[0]):
            print(f"Check idx: {pidx}")

            i = 0
            while i < n - 1:
                if len(strs[i]) <= pidx:
                    print(f"\tToo small @ {pidx}: {strs[i]} < {len(strs[i])}")
                    break

                if len(strs[i + 1]) <= pidx:
                    print(f"\tNext string too small @ {pidx}: {strs[i + i]} < {len(strs[i + i])}")
                    break

                if strs[i][pidx] != strs[i + 1][pidx]:
                    print(f"\tNot a match @ {pidx}: {strs[i]} != {strs[i + 1]}")
                    break 

                i += 1

            pidx += 1

            if i != (n - 1):
                # not a match
                print(f"\t\tNot a match => exit")
                break
        
        print(f"Return 0:{pidx-1}")
        return strs[0][0:pidx-1]


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