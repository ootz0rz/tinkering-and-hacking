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

# https://leetcode.com/problems/separate-black-and-white-balls/description/

'''
IDEA:

    We have a 2 ptr window, which just skips over all the already sorted elements

    Once we find an unsorted element, we virtually swap it and track the number of swaps
    needed as j-i, adding to our total

    Then we can shorten our window and repeat.

    Nice thing here is we don't have to modify the string or anything, we're just tracking
    # of possible 'virtual' swaps needed
'''
class Solution:
    def minimumSteps(self, s: str) -> int:
        i = 0
        j = len(s) - 1

        numSteps = 0
        while i <= j:
            print(f"START i:{i}, j:{j}, s[i:j+1]={s[i:j+1]} -- numSteps: {numSteps}")
            while s[i] == "0" and i < j:
                i += 1

            while s[j] == "1" and i < j:
                j -= 1 

            # swap and track
            numSteps += j - i
            i += 1
            j -= 1
        
        return numSteps

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minimumSteps

    check_solution_simple(
        sf,
        args=["0"],
        expected=0,
    )
    check_solution_simple(
        sf,
        args=["1"],
        expected=0,
    )
    check_solution_simple(
        sf,
        args=["01"],
        expected=0,
    )
    check_solution_simple(
        sf,
        args=["10"],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=["101"],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=["100"],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=["100000"],
        expected=5,
    )

    check_solution_simple(
        sf,
        args=["0010000011"],
        expected=5,
    )