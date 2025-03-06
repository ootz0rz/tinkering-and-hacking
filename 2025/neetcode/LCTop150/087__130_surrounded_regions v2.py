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

# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

'''
Traverse until we find a "1", then consume them and count the number of islands as we go along

We'll mark visited squares in the grid by setting them to WATER as we go too, to avoid duplicates.
'''
DIR = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]
X = "X"
O = "O"
SURR = "-"
# doesn't work
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        global DIR, X, O, SURR

        n = len(board)
        m = len(board[0])

        '''
        Idea:

        Look for any edges with an O, and then 'capture' all Os from that point outwards
        and set as SURR

        We then look through the grid again and set anything that's still O as X, since it
        was not adjacent to an O's on the edges (and thus capturable) and we return any
        SURR back to O since those are uncapturable
        '''

        return board # for easier testing
        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.numIslands

    check_solution_simple(  
        sf,
        args=[[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]],
        expected=1
    )