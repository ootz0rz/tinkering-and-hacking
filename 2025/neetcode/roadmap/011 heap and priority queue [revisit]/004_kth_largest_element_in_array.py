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

# https://neetcode.io/problems/kth-largest-element-in-an-array

'''
We want to find kth smallest, so we'll use a min-heap that will keep track of k elements at a time.

Each time we add a new element, we remove the smallest element from top of heap. So what remains is
actually the k largest elements.
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for n in nums:
            heapq.heappush(heap, n)

            while len(heap) > k:
                r = heapq.heappop(heap) # pop smallest element

        return heap[0]
        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.findKthLargest

    check_solution_simple(  
        sf,
        args=[[2,3,1,5,4], 2],
        expected=4
    )

    check_solution_simple(  
        sf,
        args=[[2,3,1,1,5,5,4], 3],
        expected=4
    )