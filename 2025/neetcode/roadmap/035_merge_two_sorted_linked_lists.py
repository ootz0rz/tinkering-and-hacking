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

# https://neetcode.io/problems/merge-two-sorted-linked-lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        # init output
        head = ListNode()
        start = head

        curL1 = list1
        curL2 = list2

        while (curL1 is not None) and (curL2 is not None):

            if curL1.val < curL2.val:
                # print("curL1: ", curL1)
                head.next = curL1
                curL1 = curL1.next
            else:
                # print("curL2: ", curL2)
                head.next = curL2
                curL2 = curL2.next
                
            head = head.next

        if curL1 is not None:
            head.next = curL1
        
        if curL2 is not None:
            head.next = curL2

        return start.next


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
        args=[[1,2,4], []],
        expected=[1,2,4],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2,4], [1,3,5]],
        expected=[1,1,2,3,4,5],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )