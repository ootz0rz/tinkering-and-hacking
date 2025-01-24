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

'''
WATCH VIDEO ?? https://neetcode.io/problems/products-of-array-discluding-self
https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview
'''
class Solution:
    '''
    Idea:

    We run into issues using division when we have 0s. There are 3 possibilities here that we care about: no zeroes, 1 zero, multiple zeroes

    No zeroes:
        We can just get the total product, and divide by our current value to get the product except self at that spot

    1 zero:
        We don't divide by 0, since that won't work...but since there's only 1 zero, and we're not including ourselves, it actually just
        means that the product except self at that spot is the total product

        Meanwhile, all other values in our array will be 0

    multiple zeros:
        The total product will always be zero, so all spots are 0 in our result array
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        # check how many zeroes and get total product for later use
        total = 1
        zeroes = 0

        # calc product without zeroes
        i = 0
        while i < l and zeroes <= 1:
            e = nums[i]

            if e == 0:
                zeroes = zeroes + 1
            else:
                total = total * e

            i = i + 1

        # 3rd case, multiple zeroes
        if zeroes > 1:
            # note: we could also reuse `nums` here
            return [0] * l
        
        for i in range(i):
            if zeroes > 0:
                # 2nd case, 1 zero
                if nums[i] == 0:
                    nums[i] = total
                else:
                    nums[i] = 0
            else:
                # first case, no zeroes to worry about
                nums[i] = total // nums[i]

        return nums

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.productExceptSelf

    # check_solution_simple(
    #     sf,
    #     args=[[1,2,3,4]],
    #     expected=[24,12,8,6]
    # )

    # check_solution_simple(
    #     sf,
    #     args=[[1,2,4,6]],
    #     expected=[48,24,12,8]
    # )

    check_solution_simple(
        sf,
        args=[[-1,1,0,-3,3]],
        expected=[0,0,9,0,0]
    )