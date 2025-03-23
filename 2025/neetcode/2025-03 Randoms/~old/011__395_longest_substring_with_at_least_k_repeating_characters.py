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
import sys

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

# WORKS but inefficient stack memory usage for when S is big
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or k > n:
            return 0
        
        sFreq = {}
        moreThanK = set()
        
        def decFreq(idx: int):
            nonlocal sFreq, moreThanK
            if idx < 0 or idx >= n:
                return
            
            c = s[idx]

            if not c in sFreq:
                return
            
            sFreq[c] -= 1

            if sFreq[c] < k and c in moreThanK:
                moreThanK.remove(c)

            if sFreq[c] <= 0:
                del sFreq[c]
        
        def incFreq(idx: int):
            nonlocal sFreq, moreThanK

            if idx < 0 or idx >= n:
                return
            
            c = s[idx]

            if not c in sFreq:
                sFreq[c] = 0
            sFreq[c] += 1

            if sFreq[c] == k:
                moreThanK.add(c)
        
        # gen initial map
        for idx in range(n):
            incFreq(idx)
        print('gen: ', sFreq, moreThanK)
        
        if len(moreThanK) == len(sFreq):
            # we're done exit early
            return n
        
        mem = {}
        def search(i, j):
            nonlocal sFreq, moreThanK, s, k, mem 
            
            print(f"-- START SEARCH: {i}, {j} = {s[i:j]} -- moreThanK: {moreThanK} -- sFreq: {sFreq}")

            if i >= j or j > n:
                print(f"\t\t out of bounds: {i} >= {j} or {j} > {n}")
                return 0
            
            if len(moreThanK) == len(sFreq):
                print(f"\t\t get cur length: morethank:{len(moreThanK)} == sFreq:{len(sFreq)}")
                return sum([v for v in sFreq.values()])
            
            if (i,j) in mem:
                print(f"\tGET ({i}, {j}) in mem: {mem}")
                return mem[(i,j)]

            print(f"ADD {i}, {j} -- MEM: {mem} -- THAN K: {moreThanK}")
            decFreq(i)
            left = search(i + 1, j)
            incFreq(i)

            decFreq(j)
            right = search(i, j - 1)
            incFreq(j)

            print(f" => COMPARE LEFT: {left} RIGHT: {right}")

            mem[(i,j)] = max(left, right)

            print(f" => ADDED ({i}, {j}) in mem: {mem}")
            return mem[(i,j)]
        
        print('end search: ', sFreq, moreThanK)
        return search(0, n)



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.longestSubstring

    check_solution_simple(
        sf,
        args=["aaabbb", 4],
        expected=0,
    )

    check_solution_simple(
        sf,
        args=["aaabbb", 3],
        expected=6,
    )

    check_solution_simple(
        sf,
        args=["aaabb", 3],
        expected=3,
    )

    check_solution_simple(
        sf,
        args=["ababbc", 2],
        expected=5,
    )