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

_SEP_ = "\n"

class Solution:

    def encode(self, strs: List[str]) -> str:
        global _SEP_
        s = []

        for w in strs:
            l = len(w)
            # s = f"{s}{l}{_SEP_}{w}"
            s.append(str(l))
            s.append(_SEP_)
            s.append(w)

        return ''.join(s)

    def decode(self, s: str) -> List[str]:
        r = []

        i = 0
        j = 0
        while i < len(s) and j < len(s):
            cur = s[j]

            if cur == _SEP_:
                num = int(s[i:j])
                word = s[j+1 : j+num+1]

                # print(_SEP_, 'found', i, j, ' -> ', num, ' -> ', word)

                i = j + 1 + num

                r.append(word)

            j = j + 1
        
        return r

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    se = s.encode
    sd = s.decode

    e = check_solution_simple(
        se,
        args=[["neet", "code", "love", "you"]],
        expected="4#neet4#code4#love3#you"
    )

    check_solution_simple(
        sd,
        args=[e],
        expected=["neet", "code", "love", "you"]
    )