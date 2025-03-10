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
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # generate graph so we can check for cyclic dependencies 
        graph = defaultdict(list) # NOTE: defaultdict is useful here so if any course doesn't show up in prerequisites, it just has empty requirements list
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        def isValid(c):
            nonlocal visited
            # check if this course has any cyclic dependencies
            if c in visited:
                return False
            
            visited.add(c)

            # check if there's any cyclic dependencies in the children here
            for n in graph[c]:
                if not isValid(n):
                    return False
                
            visited.remove(c) #backtrack -- https://leetcode.com/explore/featured/card/graph/619/depth-first-search-in-graph/3882/
            
            # we've validated this sub-graph, so we can just ignore it from now on as being valid
            # in order to do that, we just remove its children so it's not explored again in the
            # future
            graph[c] = []

            return True 
        
        # since numCourses refers to courseID as well, let's check they're all valid
        for c in range(numCourses):
            if not isValid(c):
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