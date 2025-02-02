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

# https://neetcode.io/problems/islands-and-treasure

# valid directions
_DIR = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

'''
Rough idea:

From any given cell, we want to mark it valid if it a stream originating at it can reach both oceans.

We reach pacific iff
row <= -1, col <= -1

We reach atlantic iff
row >= nr, col >= nc

So need to find a path from each cell where both the above are true

----

We can start from the edges and move our way inwards, one for each ocean, and then look at intersection of reachable cells?

For each edge cell, we can do BFS and look for the largest cell(s) reachable. These can all be marked as visited AND marked
as potential drain points. 
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        global _DIR

        nr = len(heights)        
        nc = len(heights[0])

        q = deque()

        # these 3 sets combined give us the visited set, just with a bit more info
        invalid = set()
        validPac = set()
        validAtl = set()
        
        def add_neighbour(r, c, pathStart, lastHeight):
            nonlocal heights

            # check bounds
            if r < 0 or r >= nr or c < 0 or c >= nc:
                print(f"\t\txxx OOB {(r, c)} v {(nr, nc)}")
                return
            
            # check if visited
            rc = (r, c)
            if rc in invalid:
                print(f"\t\txxx invalid! {rc in invalid}")
                return
            
            if rc in validAtl or rc in validPac:
                print(f"\t\tvvv VALID {rc}! atl: {rc in validAtl}, pac: {rc in validPac}")
                return
            
            # is our height valid?
            h = heights[r][c]
            if h < lastHeight:
                print(f"\t\txxx Invalid: {rc}")
                invalid.add(rc)
                return
            
            # search here next
            q.append((rc, pathStart))

            # mark as valid
            if pathStart % 3 == 0:
                validPac.add(rc)
            
            if pathStart % 5 == 0:
                validAtl.add(rc)

            print(f"\t\t+++ ADDING: {rc}, {pathStart}")

            return True

        # add edge items
        for ridx in range(0, nr):
            for cidx in range(0, nc):
                rc = (ridx, cidx)

                addPac = False
                addAtl = False
                if ridx == 0 or cidx == 0:
                    validPac.add(rc)
                    addPac = True
                
                if (ridx == nr-1) or (cidx == nc-1):
                    validAtl.add(rc)
                    addAtl = True

                if addPac or addAtl:
                    val = 1
                    val *= 3 if addPac else 1
                    val *= 5 if addAtl else 1
                    q.append((rc, val))

        print(f"Pacific Items: {sorted(list(validPac))}, Atlantic Items: {sorted(list(validAtl))}")

        # now we start BFS from all the edge items at the same time
        while len(q) > 0:
            print(f"Q: {sorted(list(q))}")
            for _ in range(len(q)):
                rc, pathStart = q.popleft()
                r, c = rc

                h = heights[r][c]

                # add neighbours if their height is higher
                print(f"\tFind Neighbours of ({rc}, {pathStart}={h})")
                for x, y in _DIR:
                    rx = r + x
                    cy = c + y

                    add_neighbour(rx, cy, pathStart, h)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.pacificAtlantic

    heights = [
        [4,2,7,3,4],
        [7,4,6,4,7],
        [6,3,5,3,6]
    ]
    check_solution_as_tuplesets(  
        sf,
        args=[heights],
        expected=[[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
    )

    # grid = [[1,1,0],[0,1,1],[0,1,2]]
    # check_solution_simple(  
    #     sf,
    #     args=[grid],
    #     expected=4
    # )