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

'''
Idea:

Create 2 new lists, prefix and postfix products

Then at any index i in nums, we can check prefix * postfix of neighbours in their respective arrays
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * (len(nums))
        post = [0] * (len(nums))

        # init
        pre[0] = 1
        post[-1] = 1

        l = 1
        r = len(nums) - 2

        #print(f"Pre: {pre} Post: {post} -- N: {nums}")

        while l < len(nums):
            pre[l] = pre[l - 1] * nums[l - 1]
            l += 1
        
        while r >= 0:
            post[r] = post[r + 1] * nums[r + 1]
            r -= 1

        #print(f"Pre: {pre} Post: {post} -- N: {nums}")

        # final pass
        res = []
        i = 0 
        while i < len(nums):
            res.append(pre[i] * post[i])

            i += 1

        return res
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.productExceptSelf

    check_solution_simple(  
        sf,
        args=[[1,2,3,4]],
        expected=[24,12,8,6]
    )