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

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)

        u12 = s1 & s2
        if len(u12) > 0:
            return min(u12)
        
        m1 = min(s1)
        m2 = min(s2)
        return min(
            m1 * 10 + m2,
            m2 * 10 + m1
        )
        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.waysToBuyPensPencils

    # check_solution_simple(
    #     sf,
    #     args=["((()(()()))()((()()))))()((()(()", "10111100100101001110100010001001"],
    #     expected=True,
    # )

    check_solution_simple(
        sf,
        args=[20, 10, 5],
        expected=9,
    )
