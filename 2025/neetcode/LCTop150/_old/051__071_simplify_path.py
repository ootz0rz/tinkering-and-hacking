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

# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150
PATH_SEP = '/'
CUR_PATH = '.'
PARENT = '..'
class Solution:
    def simplifyPath(self, path: str) -> str:
        global PATH_SEP, CUR_PATH, PARENT
        s = []

        i = 0
        for j,e in enumerate(path+"/"):
            #print(f"{j}={e}")
            if e == PATH_SEP:
                # read value of [i:j) and see what we should do with it
                val = path[i:j]
                
                if len(val) > 0:
                    # we've read in a value, either it's a path fragment,
                    # or one of our special cases

                    if val == PARENT:
                        # pop parent if possible
                        if len(s) > 0:
                            s.pop()
                    elif val != CUR_PATH:
                        s.append(val)

                i = j+1
        
        return "/" + "/".join(s)


        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.simplifyPath

    check_solution_simple(  
        sf,
        args=["/"],
        expected="/"
    )

    check_solution_simple(  
        sf,
        args=["/home"],
        expected="/home"
    )

    check_solution_simple(  
        sf,
        args=["/home//foo"],
        expected="/home/foo"
    )

    check_solution_simple(  
        sf,
        args=["/home/user/Documents/../Pictures"],
        expected="/home/user/Pictures"
    )