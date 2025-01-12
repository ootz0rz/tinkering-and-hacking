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

# https://neetcode.io/problems/time-based-key-value-store

'''
{
    'key': [
        (t1, val),
        (t2, val),
        (t3, val),
        ...
    ]
}
'''
class TimeMap:
    def __init__(self):
        self._table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self._table:
            self._table[key] = []

        self._table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self._table:
            return ""
        
        # search for largest value in table for this key,
        # such that the timestamp stored <= given timestamp
        vals = self._table[key]

        # do we have any possible valid values?
        if vals[0][0] > timestamp:
            return ""

        # search for next highest value, that's still smaller than the given timestamp
        left = 0
        right = len(vals) - 1

        finalVal = ""
        while left <= right:
            mid = left + ((right - left) // 2)

            t, v = vals[mid]
            
            if t > timestamp:
                # discard right
                right = mid - 1
            else:
                # found a t smaller than timestamp, so we record its value for now and keep searching
                # for something closer to the given timestamp
                finalVal = v

                # discard left
                left = mid + 1
        
        return finalVal


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = TimeMap()
    sf = s

    sf.set("foo", "bar", 1)
    assert sf.get("foo", 1) == "bar"
    assert sf.get("foo", 3) == "bar"
    sf.set("foo", "bar2", 4)
    assert sf.get("foo", 4) == "bar2"
    assert sf.get("foo", 5) == "bar2"