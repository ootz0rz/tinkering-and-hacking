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

# https://neetcode.io/problems/course-schedule

'''
If we treat each course as a node, and the prereq between them as directional edges,
then what we're looking for is a cycle in the graph of prereqs

Going to iterate through prereqs, and DFS to trace back any prereqs. Everything we
traverse, we'll add to a visited list. If we can get through the courses without
hitting a visited node again, we're good.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        n = len(prerequisites)
        visited = set()

        # gen map first
        # NOTE: not all courses will have prereqs listed!
        #       preqrequisites list is strictly an edge definition, but the number
        #       of total nodes is defined by numCourses!
        preMap = defaultdict([])
        for c, p in prerequisites:
            preMap[c].append(p)

        def check(course):
            nonlocal prerequisites, preMap

            if course in visited:
                return False # cycle
            
            if (not course in preMap) or (len(preMap[course]) == 0):
                return True # no prereqs
            
            # check this course's prereq next
            visited.add(course)

            for p in preMap[course]:
                if not check(p):
                    return False
                
            visited.remove(course)

            # we don't have to check this node ever again so can ignore its prereqs going forward
            preMap[course] = []
            
            return True

        for course in range(numCourses):
            if not check(course):
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
        args=[2, [[0,1]]],
        expected=True
    )

    check_solution_simple(  
        sf,
        args=[2, [[0,1],[1,0]]],
        expected=False
    )

    check_solution_simple(  
        sf,
        args=[3, [[1,0]]],
        expected=True
    )