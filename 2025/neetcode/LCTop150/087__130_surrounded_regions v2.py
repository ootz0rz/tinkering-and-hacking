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
Idea:

Look for any edges with an O, and then 'capture' all Os from that point outwards
and set as some temporary value, INV

We then look through the grid again and set anything that's still O as X, since it
was not adjacent to an O's on the edges (and thus capturable) and we return any
SURR back to O since those are uncapturable
'''
DIR = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]
X = "X"
O = "O"
INV = "-"
# doesn't work
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        global DIR, X, O, INV

        n = len(board)
        m = len(board[0])

        def markInvalid(r, c):
            # check bounds
            if not (0 <= r < n and 0 <= c < m):
                return
            
            if board[r][c] != O:
                return
            
            board[r][c] = INV
            for x, y in DIR:
                rx = r + x 
                cy = c + y

                markInvalid(rx, cy)

        # check rows
        for r in range(n):
            if board[r][0] == O:
                markInvalid(r, 0)

            if board[r][m - 1] == O:
                markInvalid(r, m - 1)

        # check cols
        for c in range(m):
            if board[0][c] == O:
                markInvalid(0, c)

            if board[n - 1][c] == O:
                markInvalid(n - 1, c)
        
        # now go through and mark all remaining Os as captured
        # and anything as INV back to O
        for r in range(n):
            for c in range(m):
                if board[r][c] == O:
                    board[r][c] = X
                elif board[r][c] == INV:
                    board[r][c] = O 

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