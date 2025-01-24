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

# https://neetcode.io/problems/linked-list-cycle-detection

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
            
        l1 = head

        if head.next is None:
            return False

        l2 = head.next

        while l1 is not None and l2 is not None:
            if l1 == l2:
                return True

            l1 = l1.next

            l2 = l2.next
            if l2 is not None:
                l2 = l2.next
        
        return False


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.hasCycle

    check_solution_simple(
        sf,
        args=[LN__ARRAY_TO_LL([1,2,3,4], index=1)],
        expected=True,
        # input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        # output_transform_func=LN__LL_TO_ARRAY,
    )