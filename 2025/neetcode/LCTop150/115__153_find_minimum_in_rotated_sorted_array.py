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

'''
1)
[0,1,2,3,4,5]
    L     M   R

In this case, L < M < R so both sides appear sorted. But we'll explore left side since L < M

2)
[4,5,6,7,0,1,2]
    L     M     R 

In this case, L < M > R. Left side appears sorted, but right side is going to have the min value.

3)
[7,0,1,2,3,4,6]
    L     M     R

In this case, L > M < R. Right side appears sorted, explore left side. 
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L = 0
        R = len(nums) - 1

        while L <= R:
            # we want to find a midpoint such that num[m-1] > num[m]
            m = L + ((R - L) // 2)

            if nums[m - 1] >= nums[m]:
                return nums[m]
            
            # otherwise we need to decide which side to investigate depending on scenario
            if nums[L] < nums[m]:
                if nums[m] <= nums[R]:
                    R = m - 1
                else:
                    L = m + 1 
            else:
                if nums[m] <= nums[R]:
                    R = m - 1
                else:
                    L = m + 1
        
        return -999



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.findMin

    check_solution_simple(
        sf,
        args=[[3,4,5,1,2]],
        expected=1,
    )