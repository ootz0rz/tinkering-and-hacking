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

# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot = {}
        ttos = {}
        for i in range(len(s)):
            si = s[i]
            ti = t[i]

            if (si in stot and stot[si] != ti) or (ti in ttos and ttos[ti] != si):
                return False
            
            stot[si] = ti
            ttos[ti] = si

        return True


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
