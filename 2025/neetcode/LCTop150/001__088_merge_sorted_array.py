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

# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150


'''
Two cases...

n1[i] < n2[j]:
    Consume n1[i] and leave j pointer alone

n1[i] > n2[j]:
    Consume n2[j], by transferring that value into 
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        midx = m - 1
        nidx = n - 1
        rptr = m + n - 1

        while nidx >= 0: # once nidx is 0, we've completed that array, but nums1 still has space if it reaches 0 first
            em = nums1[midx]
            en = nums2[nidx]

            if midx >= 0 and em >= en:
                # consume em, move to end
                nums1[rptr] = em
                midx -= 1
            else:
                nums1[rptr] = en
                nidx -= 1
            
            rptr -= 1



        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.coinChange

    check_solution_simple(  
        sf,
        args=[[1], 0],
        expected=0
    )

    check_solution_simple(  
        sf,
        args=[[1], 5],
        expected=5
    )

    check_solution_simple(  
        sf,
        args=[[5], 5],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=[[1,5], 10],
        expected=2
    )

    check_solution_simple(  
        sf,
        args=[[1, 5], 12],
        expected=4
    )