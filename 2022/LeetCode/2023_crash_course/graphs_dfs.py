# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4626/

import pprint
from typing import List, Optional, Dict

# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from TestHarness import *

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/number-of-provinces/
# ----------------------------------------------------------------------------------------------------------------------

def findCircleNum(self, isConnected: List[List[int]]) -> int:
    num_prov = 0

    N = len(isConnected)

    def mark_province(x):
        nonlocal isConnected, N

        isConnected[x][x] = 0
        for y, cell in enumerate(isConnected[x]):
            if cell == 1:
                isConnected[x][y] = 0
                mark_province(y)


    for x, row in enumerate(isConnected):
        if isConnected[x][x] == 1:
            mark_province(x)
            num_prov = num_prov + 1

    return num_prov

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4693/

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True
    
    for a,b in edges:
        if (a == source and b == destination) or (b == source and a == destination):
            return True

    return False 