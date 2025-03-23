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

# https://leetcode.com/problems/longest-well-performing-interval/

# Doesn't work... sliding window not good here since it's hard to figure out 
# when to bring up the rear

'''
https://leetcode.com/problems/longest-well-performing-interval/solutions/2352454/sliding-window-would-not-work-here/
https://leetcode.com/problems/longest-well-performing-interval/solutions/6567634/beat-100-0ms-prefixsum-suffixmax-slidingwindow-o-n/

Here, the sliding window does not hold because:
We do not have intrinsic 'monotonicity' in the condition we want. Basically, if one problem can be solved via sliding window, then it should satisfy: the condition unsatisfied (satisfied) in small sets => the condition unsatisfied (satisfied) in larger sets.
Unfortunately, this problem here does not have this kind of property.
'''
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        i = 0
        j = 0

        numTiring = 0
        numNormal = 0

        maxLen = 0
        while i <= j and j < len(hours):
            
            if hours[j] > 8:
                numTiring += 1
            else:
                numNormal += 1
            
            while numTiring <= numNormal and i <= j:
                si = hours[i]

                if si > 8:
                    numTiring -= 1
                else:
                    numNormal -= 1

                i += 1

            maxLen = max(maxLen, j - i + 1)

            j += 1

        return maxLen

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.longestWPI

    check_solution_simple(
        sf,
        args=[[9,9,6,0,6,6,9]],
        expected=3,
    )

    check_solution_simple(
        sf,
        args=[[6,6,9]],
        expected=1,
    )