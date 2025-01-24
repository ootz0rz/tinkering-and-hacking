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
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
        '''
        seen = set([])

        for e in nums:
            if e in seen:
                return True
            
            seen.add(e)
        
        return False

if __name__ == '__main__':
    s = Solution().hasDuplicate

    assert s([1,2,3,3]) == True
    assert s([1,2,3,4]) == False
    assert s([]) == False
    assert s([1]) == False
    assert s([1,1]) == True