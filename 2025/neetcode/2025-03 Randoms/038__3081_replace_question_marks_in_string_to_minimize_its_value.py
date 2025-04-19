from typing import List,Optional
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

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        oa = ord('a')
        hp = [[0, chr(oa + a)] for a in range(26)]

        for e in s:
            if e == "?":
                continue

            curord = ord(e) - oa
            hp[curord][0] += 1

        heapq.heapify(hp)

        #print(f"hp: {hp}")

        news = []
        letters = [] # for the lexographic sorting bit
        for e in s:
            if e == "?":
                freq, letter = heapq.heappop(hp)
                letters.append(letter)
                heapq.heappush(hp, [freq + 1, letter])
            
            news.append(e)

        letters.sort()

        j = 0
        for idx, e in enumerate(news):
            if e == "?":
                news[idx] = letters[j]
                j += 1
        
        #print(f"news: {news} < s: {s}")

        return "".join(news)
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minimizeStringValue

    check_solution_simple(
        sf,
        args=["a?a?"],
        expected="abac",
    )

    check_solution_simple(
        sf,
        args=["???"],
        expected="abc",
    )