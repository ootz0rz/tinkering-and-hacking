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

# https://neetcode.io/problems/kth-largest-integer-in-a-stream

def LC(i):
    return 2 * i

def RC(i):
    return 2 * i + 1

def PARENT(i):
    return i // 2

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = [-1] # treat as min-heap
        self.k = k

        for n in nums:
            self.add(n)

    def _heapPop(self):
        if len(self.arr) == 1:
            return
        
        if len(self.arr) == 2:
            self.arr.pop()
            return 
        
        res = self.arr[1] # save for pop

        # overwrite and move last value to root
        self.arr[1] = self.arr.pop()

        i = 1
        # bubble downwards
        while LC(i) < len(self.arr):
            rc = RC(i)
            lc = LC(i)
            if RC(i) < len(self.arr) and self.arr[rc] < self.arr[lc] and self.arr[i] > self.arr[rc]:
                # swap right child
                temp = self.arr[i]

                self.arr[i] = self.arr[rc]
                self.arr[rc] = temp

                i = rc
            elif self.arr[i] > self.arr[lc]:
                # swap left child
                temp = self.arr[i]

                self.arr[i] = self.arr[lc]
                self.arr[lc] = temp 

                i = lc
            else:
                break
        
        return res


    def add(self, val: int) -> int:
        # add to end
        self.arr.append(val)
        i = len(self.arr) - 1

        print(f"Add val: {val}, len: {i+1} > {self.k}? -- {self.arr}")

        # bubble up
        while i > 1:
            iPar = PARENT(i)
            if self.arr[i] < self.arr[iPar]:
                cur = self.arr[i]

                self.arr[i] = self.arr[iPar]
                self.arr[iPar] = cur

                i = iPar
            else:
                break

        # get kth largest...
        while len(self.arr) > self.k:
            r = self._heapPop()
            print(f"\tPop: {r}")

        # return top of heap?
        return self.arr[1]


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = KthLargest(3, [1, 2, 3, 3])
    sf = s.add

    check_solution_simple(sf, args=[3], expected=3)
    check_solution_simple(sf, args=[5], expected=3)
    check_solution_simple(sf, args=[6], expected=3)
    check_solution_simple(sf, args=[7], expected=5)
    check_solution_simple(sf, args=[8], expected=6)