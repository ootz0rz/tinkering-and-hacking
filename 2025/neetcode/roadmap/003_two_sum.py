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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

        You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

        Return the answer with the smaller index first.

        2 <= nums.length <= 1000
        -10,000,000 <= nums[i] <= 10,000,000
        -10,000,000 <= target <= 10,000,000
        '''
        
        left = 0

        diffs = {}

        while left < len(nums):
            diff = target - nums[left]
            if (diff in diffs):
                d = diffs[diff]
                if left < d:
                    return [left, d]
                else:
                    return [d, left]
            
            diffs[nums[left]] = left

            left = left + 1

if __name__ == '__main__':
    def s(result, 
          *args, **kwargs):
        r = Solution().twoSum(*args, **kwargs)

        assert result == r, f"Expected `{result}` but got `{r}`"

    s([0, 1], 
      [3,4,5,6], 7)
    
    s([0, 2], 
      [4,5,6], 10)
    
    s([0, 1], 
      [5,5], 10)