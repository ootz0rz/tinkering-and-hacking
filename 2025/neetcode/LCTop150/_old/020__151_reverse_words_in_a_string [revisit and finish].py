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

# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseWords(self, s: str) -> str:
        # reverse the string, skip extra whitespace
        i = 0
        j = len(s) - 1

        r = list(s)
        num_extra_blanks = 0
        while i < j:
            pass

        # then reverse each word in string
        return s


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.longestCommonPrefix

    check_solution_simple(  
        sf,
        args=["the sky is blue"],
        expected="blue is sky the"
    )

    check_solution_simple(  
        sf,
        args=["a good   example"],
        expected="example good a"
    )