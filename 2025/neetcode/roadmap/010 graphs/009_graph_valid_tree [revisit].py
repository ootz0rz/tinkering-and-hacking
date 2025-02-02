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
We'll check for 2 things:

1) cycles
2) all nodes are connected in the tree
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            # too many edges defined, since they're bidirectional
            return False

        visited = set()

        # gen edge map
        edgeMap = {}
        for i in range(n):
            edgeMap[i] = [] 

        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        def dfs(node, parent):
            nonlocal edges, edgeMap

            print(f"DFS: {node}")

            if node in visited:
                print(f"\t visited: {node} in {visited}")
                return False # cycle
            
            print(f"\tcheck childs: {edgeMap[node]}")
            
            visited.add(node)
            for s in edgeMap[node]:
                if s == parent:
                    # skip if we just came from here
                    continue

                if not dfs(s, node):
                    return False

            print(f" - ")
            return True

        # if everything is connected, then we should be able to DFS from
        # any single node and reach them all
        # 
        # also, we want to make sure all nodes are connected and used
        return dfs(0, -1) and len(visited) == n


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.validTree

    check_solution_simple(  
        sf,
        args=[5, [[0, 1], [0, 2], [0, 3], [1, 4]]],
        expected=True
    )

    check_solution_simple(  
        sf,
        args=[5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]],
        expected=False
    )