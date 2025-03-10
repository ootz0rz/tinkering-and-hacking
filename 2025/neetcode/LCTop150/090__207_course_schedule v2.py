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

# https://leetcode.com/problems/course-schedule/?envType=study-plan-v2&envId=top-interview-150

# O(V+E) runtime
# O(V) space

# We just want to check for cycles here basically
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # generate graph first
        # useful to use defaultdict here so it takes care of courses that are defined
        # via numcourses, but not inside prerequisites, for us
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)

        seen = set()
        def validate(idx):
            if not idx in graph:
                # no prereqs for this course so move on
                return True
            
            if idx in seen:
                return False # cycle
            
            seen.add(idx)
            for b in graph[idx]:
                if not validate(b):
                    return False
            seen.remove(idx) # backtrack along each path
            graph[idx] = [] # path validated so we can just ignore it going forward
                
            return True

        # start to iterate through each course and see if it can possibly be completed
        for idx in range(numCourses):
            if not validate(idx):
                return False

        return True

        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.canFinish

    check_solution_simple(  
        sf,
        args=[2, [[1,0],[0,1]]],
        expected=False
    )

    check_solution_simple(  
        sf,
        args=[5, [[1,4],[2,4],[3,1],[3,2]]],
        expected=True
    )