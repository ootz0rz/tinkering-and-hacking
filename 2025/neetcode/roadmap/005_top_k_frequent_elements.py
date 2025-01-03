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

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count num of occurances
        count = {}
        for e in nums:
            count[e] = 1 + count.get(e, 0)

        print('count', count)

        # bucket, where idx = # of occurances
        # buckets = [[]] * (len(nums) + 1) # add one for placeholder 0 occurances
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for number, freq in count.items():
            buckets[freq].append(number)

        print('buckets', buckets)

        # finally, generate flat list from largest to smallest, up to k elements
        res = []
        bidx = len(buckets) - 1
        while bidx > 0 and k > 0:
            if len(buckets[bidx]) > 0:
                res.extend(buckets[bidx])
                k = k - len(buckets[bidx]) # k elements max
            bidx = bidx - 1

        print('res', res)
        return res
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    
    from TestHarness import *

    s = Solution()
    sf = s.topKFrequent

    # sf([1,2,2,4,3,3,3], 2)
    sf([4,1,-1,2,-1,2,3], 2)