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

# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
SEP = set(["(", ")", " "])
OPS = set(["+", "-"])
class Solution:
    def calculate(self, s: str) -> int:        
        vals = []
        op = None

        i = 0
        j = 0
        
        capVal = False
        while j <= len(s):
            if j == len(s):
                e = " "
            else:
                e = s[j]

            issep = e in SEP
            isplus = e == '+'
            isneg = e == '-'

            print(f"s[j:{j}] = {e}, sep? {issep} plus? {isplus} neg? {isneg}, s[i:{i}-j:{j}] = {s[i:j]}")

            if e in SEP or isplus or isneg:
                # we encountered a boundary 
                if i != j:
                    val = s[i:j]

                    if op == '-':
                        print(f"\t\tNEGATE VAL=>{val} => {f'-{val}'}")
                        val = f"-{val}"
                        op = '+'

                    vals.append(int(val))
                    print(f"\tval=[{val}]")

                # if this is an operator, lets track it
                if isplus:
                    print(f"\top=[+]")
                    op = "+"
                elif isneg:
                    print(f"\top=[-]")
                    op = "-"

                # if we have two values saved, and an operator, lets process that
                if len(vals) == 2 and op is not None:
                    right = vals.pop()
                    left = vals.pop()

                    if op == '+':
                        vals.append(left + right)
                        print(f"\tPROCESS=[{left} + {right}]={vals}")
                    elif op == '-':
                        vals.append(left - right)
                        print(f"\tPROCESS=[{left} - {right}]={vals}")
                
                i = j + 1
            
            # if e is a number
            j = j + 1
        return vals[0]

        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.calculate

    check_solution_simple(  
        sf,
        args=[" 2-1"],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=["1 + 1"],
        expected=2
    )

    check_solution_simple(  
        sf,
        args=["(1+2)"],
        expected=3
    )

    check_solution_simple(  
        sf,
        args=["(1+2+(5+4))"],
        expected=(1+2+5+4)
    )

    check_solution_simple(  
        sf,
        args=["-1"],
        expected=-1
    )

    check_solution_simple(  
        sf,
        args=["-1+3"],
        expected=2
    )

    ## Ugh forgot about this case...
    ## can't just ignore () then, have to either recurse or build a stack I guess of vals to process?
    check_solution_simple(  
        sf,
        args=["-(2+3)"],
        expected=-5
    )