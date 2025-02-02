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

# https://neetcode.io/problems/surrounded-regions

# valid directions
_DIR = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

O = 'O'
X = 'X'
UNC = '-'

'''
Rough idea:

We'll traverse the edges to look for O's

We then DFS from the edges outwards, and mark all those cells as uncapturable.

We can then capture the remainder O's
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        global _DIR, O, X, UNC

        nr = len(board)
        nc = len(board[0])

        def search_and_mark_unc(x, y):
            nonlocal board

            # check bounds
            if x < 0 or x >= nr or y < 0 or y >= nc:
                return

            # ignore cell?
            cell = board[x][y]

            print(f"\tSearch and mark: {x}, {y} = {cell}")
            if cell == X or cell == UNC:
                return
            
            print(f"\t\t -> MARKING")
            board[x][y] = UNC

        # top and bottom rows
        for ridx in (0, nr-1):
            for cidx, cell in enumerate(board[ridx]):
                print(f"TB Check: {ridx}, {cidx} = {cell}")
                if cell == X or cell == UNC:
                    continue

                board[ridx][cidx] = UNC
                for x, y in _DIR:
                    search_and_mark_unc(ridx + x, cidx + y)

        # first and last columns
        for ridx in range(nr):
            for cidx in (0, nc-1):
                cell = board[ridx][cidx]
                print(f"FL Check: {ridx}, {cidx} = {cell}")
                if cell == X or cell == UNC:
                    continue
                
                board[ridx][cidx] = UNC
                for x, y in _DIR:
                    search_and_mark_unc(ridx + x, cidx + y)

        # final marking
        for ridx, row in enumerate(board):
            for cidx, cell in enumerate(row):
                if cell == O:
                    print(f"Mark captured: {ridx},{cidx}")
                    board[ridx][cidx] = X

        for ridx, row in enumerate(board):
            for cidx, cell in enumerate(row):
                if cell == UNC:
                    print(f"Mark uncapturable: {ridx},{cidx}")
                    board[ridx][cidx] = O

        print(f"Board final: {board}")



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.solve

    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","X","X","O"]
    ]
    check_solution_as_tuplesets(  
        sf,
        args=[board],
        expected=[
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","O"]
        ]
    )

    # grid = [[1,1,0],[0,1,1],[0,1,2]]
    # check_solution_simple(  
    #     sf,
    #     args=[grid],
    #     expected=4
    # )