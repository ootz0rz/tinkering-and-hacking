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

# ------------ ListNode
# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from LinkedList import *
# ------------ ListNode

# https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2 

        res = ListNode()

        head = res

        # traverse both first
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                # consume l2 since its smaller
                res.next = l2
                l2 = l2.next
            else:
                # consume l1
                res.next = l1
                l1 = l1.next

            res = res.next

        # capture remainder
        if l1:
            res.next = l1
        if l2:
            res.next = l2
            
        return head.next


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.mergeTwoLists

    check_solution_simple(
        sf,
        args=[[1,2,4], [1,3,4]],
        expected=[1,1,2,3,4,4],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )