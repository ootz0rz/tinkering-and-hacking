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

# https://neetcode.io/problems/count-connected-components

'''
We're basically looking for how many graphs are formed by the nodes/edges given.

I think we can do a DFS for each pairing in edges, and keep track of what was visited

As we continue to traverse the edges, if we find anything already visited, its part of
a previous graph. But if anything is not visited, it's a new component and we can track
the number.
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0

        # gen map
        emap = {}
        for i in range(n):
            emap[i] = []

        for a, b in edges:
            emap[a].append(b)
            emap[b].append(a)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for c in emap[node]:
                dfs(c)

        for i in range(n):
            if not i in visited:
                count = count + 1
                dfs(i)

        return count


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.countComponents

    check_solution_simple(  
        sf,
        args=[3, [[0,1], [0,2]]],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=[6, [[0,1], [1,2], [2,3], [4,5]]],
        expected=2
    )