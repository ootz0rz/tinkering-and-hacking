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

# https://neetcode.io/problems/daily-temperatures
# https://leetcode.com/problems/daily-temperatures/description/

'''
Input: temperatures = 
[30,38,30,36,35,40,28]
  0, 1, 2, 3, 4, 5, 6

Output: [1,4,1,2,1,0,0]

Idea is we place every visited element into a stack. When we go onto the next element, we check if it's bigger than any of the elements
at the end of the stack. If it is, we pop them...and write the result to our result array.

Our stack will track both value and idx to make the calc easier. We could also do two stacks, one for val one for index, and treat 
them as one... but a tuple is easier to work with here
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        res = [0] * n

        stack = [] # (temp, idx)

        for i, e in enumerate(temperatures):

            while (len(stack) > 0) and e > stack[-1][0]:
                # current element is larger than end of stack
                me, mi = stack.pop()
                res[mi] = i - mi
            
            # finally add ourselves to end of stack
            stack.append((e, i))
        
        return res


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.dailyTemperatures

    check_solution_simple(
        sf,
        args=[[30,38,30,36,35,40,28]],
        expected=[1,4,1,2,1,0,0]
    )

    check_solution_simple(
        sf,
        args=[[22,21,20]],
        expected=[0,0,0]
    )