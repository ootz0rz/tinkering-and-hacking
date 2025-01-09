from typing import List
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

# https://neetcode.io/problems/valid-sudoku
# https://leetcode.com/problems/valid-sudoku/description/
'''

'''
_BLANK_ = "."
class Solution:
    def getSquareNum(self, x, y):
        return ((x // 3) * 3) + (y // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkRows = defaultdict(set)
        checkCols = defaultdict(set)
        checkSquares = defaultdict(set)

        for cidx, col in enumerate(board):
            for ridx, cellVal in enumerate(board[cidx]):
                if cellVal == _BLANK_:
                    continue

                print(f"C: {cidx} R: {ridx} => {cellVal}")
                if cellVal in checkRows[ridx]:
                    # print(f"\t exists in row: {ridx} => {checkRows[ridx]}")
                    return False
                
                if cellVal in checkCols[cidx]:
                    # print(f"\t exists in col: {cidx} => {checkCols[cidx]}")
                    return False
                
                square = self.getSquareNum(cidx, ridx)
                if cellVal in checkSquares[square]:
                    # print(f"\t exists in square: {square} => {checkSquares[square]}")
                    return False

                checkRows[ridx].add(cellVal)
                checkCols[cidx].add(cellVal)
                checkSquares[square].add(cellVal)
        
        return True

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isValidSudoku

    check_solution_simple(
        sf,
        args=[[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]],
        expected=True
    )

    check_solution_simple(
        sf,
        args=[[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]],
        expected=False
    )
