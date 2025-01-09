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

# https://neetcode.io/problems/evaluate-reverse-polish-notation
# 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for e in tokens:
            if e == "+":
                right = stack.pop()
                left = stack.pop()

                stack.append(left + right)
            elif e == "-":
                right = stack.pop()
                left = stack.pop()

                stack.append(left - right)
            elif e == "*":
                right = stack.pop()
                left = stack.pop()

                stack.append(left * right)
            elif e == "/":
                right = stack.pop()
                left = stack.pop()

                stack.append(int(left / right)) # NOTE we don't use // since it does FLOOR division, and we want to truncate int division instead
            else:
                stack.append(int(e))

                # print("\t++STACK: ", stack)

                continue
            
            # print(f"OP STACK [L:{left}] [{e}] [R:{right}] => ")
            # print("\t##STACK: ", stack)
        
        return stack.pop()


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.evalRPN

    check_solution_simple(
        sf,
        args=[["10","6","9","3","+","-11","*","/","*","17","+","5","+"]],
        expected=22
    )