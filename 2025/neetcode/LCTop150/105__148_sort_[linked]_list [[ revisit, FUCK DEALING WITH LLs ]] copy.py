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

# ------------ BinaryTree
# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from LinkedList import *
# ------------ BinaryTree

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        def bifurcateAndGetMid(node):
            print(f"Bifurcate: {node.__all__()}")
            
            # prev = node
            # while node and node.next:
            #     prev = prev.next 
            #     node = node.next.next 

            # mid = prev.next
            # prev.next = None

            # print(f"\t -> mid: {mid}")
            # return mid
            midPrev = None
            while node and node.next:
                midPrev = node if not midPrev else midPrev.next
                node = node.next.next
            mid = midPrev.next
            midPrev.next = None

            print(f"\t -> mid: {mid}")
            return mid
        
        def sort(n):
            print(f"Sort: {n.__all__()}")
            mid = bifurcateAndGetMid(n)

            left = sort(n)
            right = sort(mid)

            return merge(left, right)

        def merge(n1, n2):
            start = ListNode()

            c = start
            while n1 is not None and n2 is not None:
                if n1.val > n2.val:
                    c.next = n2
                    n2 = n2.next
                else:
                    c.next = n1
                    n1 = n1.next
                c = c.next

            # take care of any remainder
            c.next = n1 if n1 is not None else n2
            
            return start.next
        
        return sort(head)



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.sortList

    check_solution_simple(
        sf,
        args=[LN__ARRAY_TO_LL([4,2,1,3])],
        expected=[1,2,3,4],
        # input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )
