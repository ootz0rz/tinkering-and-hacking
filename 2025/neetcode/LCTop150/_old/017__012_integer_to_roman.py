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

valMap = [
    (1000, 'M'),
    (900, "CM"),
    (500, 'D'),
    (400, "CD"),
    (100, 'C'),
    (90, "XC"),
    (50, 'L'),
    (40, "XL"),
    (10, 'X'),
    (9, "IX"),
    (5, 'V'),
    (4, "IV"),
    (1, 'I'),
]

# https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""

        for digits, word in valMap:
            if num == 0:
                break

            count = num // digits
            num = num % digits

            s += (word * count)

            #print(f"digits: {digits}, word: {word} | count: {count} num: {num} s: {s}")

        return s
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.intToRoman

    check_solution_simple(  
        sf,
        args=[1994],
        expected="MCMXCIV"
    )

    check_solution_simple(  
        sf,
        args=[2],
        expected="II"
    )

    check_solution_simple(  
        sf,
        args=[4],
        expected="IV"
    )