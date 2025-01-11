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

# https://neetcode.io/problems/car-fleet
# https://leetcode.com/problems/car-fleet/description/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # generate pos+speed tuples in reverse sort order
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append((position[i], speed[i]))
    
        posSpeed.sort(reverse=True, key=lambda x: x[0]) # sort in reverse...or could just enumerate in reverse below too

        # calc end position and see if we join up with the next one
        previousTimings = []
        for i, (p, s) in enumerate(posSpeed):
            #print(f"i: {i}, p: {p}, s: {s}")

            # We calculate our current car's time to target
            # 
            # If our curtime is <= to the smallest recorded previous timing, then
            # we know that we can never catch up, so we're a new "fleet"
            curTime = (target - p) / s
            if len(previousTimings) == 0 or curTime > previousTimings[-1]:
                previousTimings.append(curTime)

        return len(previousTimings)




if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.carFleet

    check_solution_simple(
        sf,
        args=[10, [4,1,0,7], [2,2,1,1]],
        expected=3
    )