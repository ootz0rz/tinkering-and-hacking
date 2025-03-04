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

# https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # since k can be stupid large, makes sense for us to bound it to n = size of LL
        if not head:
            return head
        
        # get length of LL
        n = 1
        p = head
        while p.next:
            n += 1
            p = p.next

        # if we're just an element of 1, nothing to do
        if n <= 1:
            return head
        
        print(f"Size of list: {n}, k: {k} => {k % n}")
        print(f"p: {p} head: {head}")

        # once we get here, p is the end and head is the start
        #
        # so we need to traverse to newHead which will be k%n 
        # from the end of the list
        #
        # that then becomes the new head, and we continue to
        # traverse to the end to attach the previous head there
        # and finally we make sure that whatever is before newHead
        # has its next value set to None
        newHead = None
        

        return newHead

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.rotateRight

    check_solution_simple(
        sf,
        args=[[], 0],
        expected=[],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1], 5],
        expected=[1],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2], 3],
        expected=[2,1],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2,3], 1],
        expected=[2,3,1],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2,3,4,5], 2],
        expected=[4,5,1,2,3],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )