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

# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == '.':
                    continue

                if cell in rows[r]:
                    return False
                
                if cell in cols[c]:
                    return False
                
                x = r // 3
                y = c // 3
                xy = (x,y)
                #print(f"\t{x},{y} = {cell} in {squares[xy]}")
                if cell in squares[xy]:
                    return False
                
                rows[r].add(cell)
                cols[c].add(cell)
                squares[xy].add(cell)
        
        # print(f"Rows: {list(list(rows[r]) for r in rows)}")
        # print(f"Cols: {list(list(cols[c]) for c in cols)}")
        # print(f"Squa: {squares}")
        return True


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.isValidSudoku

    board = \
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

    check_solution_simple(  
        sf,
        args=[board],
        expected=False
    )
