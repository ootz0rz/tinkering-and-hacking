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

# https://neetcode.io/problems/combinations-of-a-phone-number

MAP = {
    "1": "",
    "2": "abc",
    "3": "def", 
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": "+",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        global MAP

        res = []
        temp = ""

        def find(idx):
            nonlocal res, temp

            if idx == len(digits):
                res.append(temp)
                return

            for e in MAP[digits[idx]]:
                temp = temp + e
                find(idx + 1)
                temp = temp[:-1]
        
        if len(digits) > 0:
            find(0)

        return res 

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.letterCombinations

    check_solution_simple(  
        sf,
        args=[""],
        expected=[]
    )

    check_solution_simple(  
        sf,
        args=["34"],
        expected=["dg","dh","di","eg","eh","ei","fg","fh","fi"]
    )