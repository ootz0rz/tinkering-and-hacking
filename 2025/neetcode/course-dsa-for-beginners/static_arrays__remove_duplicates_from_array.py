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

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Idea:
            
        Since the list nums is sorted, we can iterate through... once we find a dupe, we skip to the next non-dupe and move it in place of the first dupe...then iterate

        https://neetcode.io/solutions/remove-duplicates-from-sorted-array
        '''
        l = len(nums)
        if l == 0:
            return 0
        
        left = 0
        right = 1

        nL = nums[left]

        while right < l: 
            nR = nums[right]

            if nR != nL:
                left = left + 1
                nL = nums[left] = nR

            right = right + 1

        return left + 1

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.removeDuplicates

    check_solution_simple(
        sf,
        args=[[1,1,2]],
        expected=2
    )

    check_solution_simple(
        sf,
        args=[[0,0,1,1,1,2,2,3,3,4]],
        expected=5
    )