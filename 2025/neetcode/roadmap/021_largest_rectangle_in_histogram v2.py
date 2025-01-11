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

# https://neetcode.io/problems/largest-rectangle-in-histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # (idx, height)

        maxArea = 0
        
        for i, h in enumerate(heights):
            
            si, sh = i, h

            while stack and h < stack[-1][1]:
                # our current height is less than the top of stack, so we pop it and calculate it's area
                # we know that by virtue of having its value in the stack, it can't extend to the left,
                # it can only extend up to our current index
                si, sh = stack.pop()
                
                area = sh * (i - si)

                maxArea = max(area, maxArea)

            # note that we set the "start" index of this new height as the last value we popped out
            # because we know that h is strictly smaller than that value, so it can be extended back
            # as far as that popped values' index
            #
            # if the stack was empty, si = i
            stack.append((si, h))

        # finally process any remaining items in stack
        # 
        # we already set their "start" indices here as far back as they can go, so we just need to
        # calc their area by extending to the end of the histogram
        for (si, sh) in stack:
            maxArea = max(maxArea, sh * (n - si))

        return maxArea


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.largestRectangleArea

    check_solution_simple(
        sf,
        args=[[4]],
        expected=4
    )

    check_solution_simple(
        sf,
        args=[[2,1]],
        expected=2
    )

    check_solution_simple(
        sf,
        args=[[1,2]],
        expected=2
    )

    check_solution_simple(
        sf,
        args=[[2,2,2]],
        expected=6
    )

    check_solution_simple(
        sf,
        args=[[2,1,5,6,2,3]],
        expected=10
    )