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
import sys

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        idx = 0
        def validate(minVal, maxVal): #O(n) time and space
            nonlocal idx, preorder

            if idx == len(preorder):
                return True # done
            
            rootVal = preorder[idx]

            print(f"Validate [{idx}]: {minVal} < {rootVal} < {maxVal}")
            if not (minVal < rootVal < maxVal):
                return False

            # since with preorder, with how our input is given, we don't know
            # if the next is gonna be the left or right side
            #
            # so we check both possible conditions on it, and see if at least
            # one passes
            idx += 1
            print(f"\t Left[{idx}]: min={minVal}, max={rootVal}")
            left = validate(minVal, rootVal)
            print(f"\t Right[{idx}]: min={minVal}, max={rootVal}")
            right = validate(rootVal, maxVal)

            return left or right

        return validate(float('-inf'), float('inf'))


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.verifyPreorder

    check_solution_simple(
        sf,
        args=[[5,2,1,3,6]], 
        expected=True,
    )

    check_solution_simple(
        sf,
        args=[[5,2,6,1,3]], 
        expected=False,
    )
