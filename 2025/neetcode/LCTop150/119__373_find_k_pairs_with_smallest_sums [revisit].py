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

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150

'''
Idea:

We'll use a minheap to track smallest values.

We'll start generating every possible pairing until we have k pairs, treating this almost like a branching
tree traversal, we want to go down to height=k
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        
        # let's init the heap with the first pairing
        i = 0
        j = 0
        heapq.heappush(h, (nums1[i] + nums2[j], i, j))

        # now we need to add every subsequent pair per layer
        # which is one or both of:
        #   nums1[i+1], nums2[j]   AND   nums1[i], nums2[j + 1]
        #
        # we do this until either we've gone through k levels, or we've exhausted everything in our heap
        # at each level, we take the smallest value we have so far and add it as an answer
        # leaving us with the remainder to evaluate at next level
        o = []

        # finally we need to make sure we don't visit the same node twice
        visited = set()
        while len(h) > 0 and k > 0:
            curSum, i, j = heapq.heappop(h)
            o.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

            k -= 1
        
        return o

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.kSmallestPairs

    check_solution_simple(
        sf,
        args=[[1,7,11], [2,4,6], 3],
        expected=[[1,2],[1,4],[1,6]],
    )