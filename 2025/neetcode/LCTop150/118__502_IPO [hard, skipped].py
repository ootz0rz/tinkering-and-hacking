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

# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=top-interview-150 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # NOTE: python uses a min-heap so we can just maintain k elements in our
        #       heap since we'll always remove the smallest one first, so the k
        #       largest elements remain in heap
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.findKthLargest

    check_solution_simple(
        sf,
        args=[[3,2,1,5,6,4], 2],
        expected=5,
    )