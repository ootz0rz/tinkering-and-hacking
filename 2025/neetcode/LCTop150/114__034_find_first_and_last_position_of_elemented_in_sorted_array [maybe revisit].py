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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1

        def find(L, R, findStart=True):
            nonlocal nums
        
            while L <= R:
                m = L + ((R - L) // 2)

                if nums[m] == target:
                    # are we at start/end?
                    if findStart:
                        if m == L or nums[m-1] < target:
                            # we're at start
                            return m
                        # else keep searching left side
                        R = m - 1
                    else:
                        if m == R or nums[m+1] > target:
                            # we're at end
                            return m
                        # else keep searching right side
                        L = m + 1
                elif nums[m] > target:
                    # search left side
                    R = m - 1
                else:
                    L = m + 1
        
            return -1

        return [
            find(0, n, True),
            find(0, n, False)
        ]


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.searchRange

    check_solution_simple(
        sf,
        args=[[5,7,7,8,8,10], 8],
        expected=[3,4],
    )