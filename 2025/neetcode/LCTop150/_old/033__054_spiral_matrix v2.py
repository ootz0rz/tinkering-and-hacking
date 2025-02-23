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

# https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        Lc = 0
        Rc = len(matrix[0])

        Tr = 0 
        Br = len(matrix)
        
        n = ((Rc+1) * (Br+1))

        currow = 0
        curcol = 0
        res = []
        while Lc < Rc and Tr < Br:
            print(f"Start Cycle, Lc:{Lc} < Rc:{Rc} && Tr:{Tr} < Br:{Br}")
            # go from left to right across current row
            currow = Tr
            curcol = Lc
            print()
            while curcol < Rc:
                print(f"\t [1] L -> R, col:{curcol} <= Rc:{Rc} | row:{currow}")
                res.append(matrix[currow][curcol])
                curcol += 1
            
            Rc -= 1           
            curcol = Rc
            
            # now go down the column
            print()
            while currow < Br:
                print(f"\t [2] T -> B, col:{curcol} | row:{currow} <= Br:{Br}")
                res.append(matrix[currow][curcol])
                currow += 1

            
            Br -= 1
            currow = Br
            # currow -= 2

            # now reverse across current row, right to left
            print()
            while curcol > Lc:
                print(f"\t [3] R -> L, col:{curcol} >= Lc:{Lc} | row:{currow}")
                res.append(matrix[currow][curcol])
                curcol -= 1

            
            Lc += 1
            curcol = Lc
            # curcol += 2
            
            # and finally, move up the column to top
            print()
            while currow >= Tr:
                print(f"\t [3] B -> T, col:{curcol} | row:{currow} > Tr:{Tr}")
                res.append(matrix[currow][curcol])
                currow -= 1
            Tr += 1
            print(f"END Cycle, Lc:{Lc} < Rc:{Rc} && Tr:{Tr} < Br:{Br} => {res}")
        
        return res


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.spiralOrder

    board = [[1,2,3],[4,5,6],[7,8,9]]

    check_solution_simple(  
        sf,
        args=[board],
        expected=[1,2,3,6,9,8,7,4,5]
    )
