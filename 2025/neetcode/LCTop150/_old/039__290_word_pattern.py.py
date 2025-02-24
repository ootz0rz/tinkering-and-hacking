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

# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
_DELIM = ' '
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        global _DELIM 

        # generate mapping for s as words
        sp = s.split(_DELIM) # NOTE if need be we could do this manually too but meh

        if len(pattern) != len(sp):
            return False

        ptos = {}
        stop = {}

        for i in range(len(pattern)):
            pi = pattern[i]
            si = sp[i] 

            if (pi in ptos and ptos[pi] != si) or (si in stop and stop[si] != pi):
                return False
            
            ptos[pi] = si
            stop[si] = pi
        
        return True

        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.wordPattern

    check_solution_simple(  
        sf,
        args=["a", "b"],
        expected=True
    )

    # check_solution_simple(  
    #     sf,
    #     args=["a", "abc"],
    #     expected=True
    # )

    check_solution_simple(  
        sf,
        args=["ab", "abc def"],
        expected=False
    )

    check_solution_simple(  
        sf,
        args=["ab", "abc"],
        expected=False
    )
