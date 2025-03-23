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

'''
Idea we do sliding window with a different target size until we can't 
create a valid set anymore
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or k > n:
            return 0

        d = set()
        sFreq = {}
        moreThanK = set()

        def countNumLetters(substr: str) -> int: # O(n)
            nonlocal d

            d.clear()
            for c in substr:
                d.add(c)
            
            return len(d)
        
        def clearFreq(): # O(1)
            nonlocal sFreq, moreThanK
            sFreq.clear()
            moreThanK.clear()
        
        def decFreq(idx: int): # O(1)
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
        
        def incFreq(idx: int): # O(1)
            nonlocal sFreq, moreThanK

            if idx < 0 or idx >= n:
                return
            
            c = s[idx]

            if not c in sFreq:
                sFreq[c] = 0
            sFreq[c] += 1

            if sFreq[c] == k:
                moreThanK.add(c)
        
        maxUniqueChars = countNumLetters(s) # O(n) run, O(n) space

        print(f"Max Unique Num of Chars: {maxUniqueChars}")

        maxLen = 0
        for curUniqueCharsTarget in range(1, maxUniqueChars+1): # O(max unique) => O(26)
            i = 0
            j = 0
            clearFreq()

            curMaxLen = 0
            while i <= j and j < n: # O(n)
                ci = s[i]
                cj = s[j]

                # incFreq(j)

                print(f"TARGET: {curUniqueCharsTarget} => s={s} s[i]:s[j]={s[i]}:{s[j]} s[{i}:{j}+1]={s[i:j+1]}")

                if len(sFreq) > curUniqueCharsTarget:
                    decFreq(i)
                    i += 1
                else:
                    incFreq(j)
                    j += 1

                print(f"\t len({sFreq}) = {len(sFreq)} > {curUniqueCharsTarget}, moreThanK:{moreThanK}={len(moreThanK)}")
                if len(moreThanK) == len(sFreq) == curUniqueCharsTarget: # all chars are more than k in count
                    curMaxLen = max(curMaxLen, sum([v for v in sFreq.values()]))
            
            maxLen = max(maxLen, curMaxLen)
         
        return maxLen # O(n) + O(26 * n) = O(26 * 2n) = O(n)




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

    check_solution_simple(
        sf,
        args=["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 2],
        expected=52,
    )