from typing import List, Optional, Self, Set, Dict
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

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150

_MAP = {
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
    "0": [],
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        global _MAP

        res = []
        n = len(digits)
        path = []

        def gen(idx):
            nonlocal digits, n 

            #print(f"\t{idx}: {path}")

            if idx == n:
                #print(f"\t\t END PATH {idx} == {n} => {path}")
                res.append("".join(path))
                return
            
            #print(f"\t\tGen Children: {_MAP[digits[idx]]}")
            for c in _MAP[digits[idx]]:
                path.append(c)
                gen(idx + 1, path)
                path.pop()
        
        if len(digits) > 0:
            #print(f"Start Gen: ", digits)
            gen(0)

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
        args=["2"],
        expected=["a", "b", "c"]
    )

    check_solution_simple(  
        sf,
        args=["23"],
        expected=["ad","ae","af","bd","be","bf","cd","ce","cf"]
    )