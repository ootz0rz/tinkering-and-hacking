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

# https://neetcode.io/problems/decode-ways

'''
Valid number formats:

    1-9
    1+0-9
    2+0-6
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        o0 = ord('0')
        o7 = ord('6')

        def _dec(i, mem):
            if i in mem:
                return mem[i]
            
            e = s[i]
            if e == '0':
                # not a valid starting letter, end this path
                return 0
            
            res = _dec(i + 1, mem)
            if (i + 1) < len(s) and \
            ( \
                (e == '1') or \
                (e == '2' and o0 <= ord(s[i + 1]) <= o7) \
            ):
                res = res + _dec(i + 2, mem)
            
            mem[i] = res

            return mem[i]
        
        return _dec(0, {len(s): 1})

        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.numDecodings

    check_solution_simple(  
        sf,
        args=["0"],
        expected=0
    )

    check_solution_simple(  
        sf,
        args=["1"],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=["01"],
        expected=0
    )

    check_solution_simple(  
        sf,
        args=["12"],
        expected=2
    )

    check_solution_simple(  
        sf,
        args=["101"],
        expected=1
    )