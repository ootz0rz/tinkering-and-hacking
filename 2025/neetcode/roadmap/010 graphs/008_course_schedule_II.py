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

# https://neetcode.io/problems/course-schedule-ii

'''
Similar to the last one

We can iterate through all the courses, and DFS on them. If we reach a cycle, we know
we can't take all the courses.

Otherwise, we can just add the DFS elements to a result list and return that at the end.
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        n = len(prerequisites)
        visited = set()
        used = set()
        outPath = []

        # gen map of prereqs
        preMap = {}
        for c, p in prerequisites:
            if not c in preMap:
                preMap[c] = []
                
            preMap[c].append(p)
        

        # DFS check
        def check(course):
            nonlocal prerequisites

            print(f"\t check: {course}, visited: {visited}, used: {used}")

            if course in visited:
                print(f"\t\t -> Visited! {visited}")
                return False # cycle
            
            if course in used:
                print(f"\t\t -> Used! {used}")
                return True

            if course < 0 or course >= numCourses:
                print(f"\t\t -> No Prereq! {course}, n: {n}")
                return True # no prereqs
            
            if not course in preMap:
                preMap[course] = []
            
            # check prereqs
            visited.add(course)
            for p in preMap[course]:
                print(f"\t\t -> CHECK PREREQ: {p} -- premap[{course}]: {preMap[course]}")
                if not check(p):
                    print(f"\t\t\t -> FAILED")
                    return False
            visited.remove(course)

            # finally, add to our path
            used.add(course)
            outPath.append(course)

            return True
        
        for course in range(numCourses):
            print(f"Course: {course} -- {preMap}")
            if not check(course):
                print("-> FAILED")
                return []
            
        return outPath


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.findOrder

    check_solution_simple(  
        sf,
        args=[3, [[1,0]]],
        expected=[0, 1, 2]
    )

    check_solution_simple(  
        sf,
        args=[4, [[1,0],[2,0],[3,1],[3,2]]],
        expected=[0,1,2,3]
    )