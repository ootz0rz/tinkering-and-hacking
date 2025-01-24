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

# https://neetcode.io/problems/longest-repeating-substring-with-replacement

'''
Thoughts:

Sliding window, where we move right until num replacements > k

We replace the least frequently occuring characters in our current window. Max length is then, the max of all
windows such that num_chars = |num of most frequently occuring characters| + |L| where 0 <= L <= k
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i = 0
        j = 0

        maxLen = 0

        freqs = {}
        maxCount = 0
        while i <= j and j < len(s):
            cj = s[j]

            # update freq
            freqs[cj] = 1 + freqs.get(cj, 0)

            # track max occurance
            maxCount = max(maxCount, freqs[cj])

            # curcount - max > k?
            while ((j - i + 1) - maxCount) > k:
                ci = s[i]

                freqs[ci] -= 1

                i = i + 1

            maxLen = max(maxLen, j - i + 1)

            j = j + 1

        return maxLen


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.characterReplacement

    check_solution_simple(
        sf,
        args=["XYYX", 2],
        expected=4
    )

    check_solution_simple(
        sf,
        args=["AAABABB", 1],
        expected=5
    )


    