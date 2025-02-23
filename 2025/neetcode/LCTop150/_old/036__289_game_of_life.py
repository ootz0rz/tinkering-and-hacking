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

# https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150
'''
2 pass?

Process lives and deads by calc their neighbours...then another pass to set result?
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        __DIR = [
            (0, 1),
            (-1, 0),
            (1, 0),
            (0, -1),

            (1, -1),
            (-1, 1),
            (1, 1),
            (-1, -1),
        ]

        n = len(board)
        m = len(board[0])

        def getN(x, y):
            nonlocal n, m, board, __DIR

            N = 0
            for dx, dy in __DIR:
                sx = x + dx
                sy = y + dy

                if (sx >= 0 and sx < n) and (sy >= 0 and sy < m):
                    if board[sx][sy] > 0:
                        N += 1
            
            return N
        
        # process
        for x in range(n):
            for y in range(m):
                N = getN(x, y)
                cell = board[x][y]

                # NOTE:
                #   we could also replace this with something like -1 if cell==0 and N==3
                #   and then 2 if N==(2 or 3) and cell==1
                #   
                #   that would simplify the check a tiny bit in the results loop below
                #   and get rid of the max check below
                if cell == 0:
                    board[x][y] = -N
                else:
                    board[x][y] = max(1, N) # just in case a cell has 0 neighbours, it's still at least a "1" for self right now
        
        #print(board)

        # result
        for x in range(n):
            for y in range(m):
                cell = board[x][y]

                if cell == 2 or cell == 3 or cell == -3:
                    board[x][y] = 1
                else:
                    board[x][y] = 0

        return board



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.gameOfLife

    check_solution_simple(  
        sf,
        args=[[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]],
        expected=[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    )

    sf([[1,0,0,0,0,1],[0,0,0,1,1,0],[1,0,1,0,1,0],[1,0,0,0,1,0],[1,1,1,1,0,1],[0,1,1,0,1,0],[1,0,1,0,1,1],[1,0,0,1,1,1],[1,1,0,0,0,0]])
