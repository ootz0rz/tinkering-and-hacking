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

from BinaryTree import *
# ------------ BinaryTree

# https://neetcode.io/problems/count-good-nodes-in-binary-tree

'''
As we traverse, pass down the max value in the path we've travelled

If max <= cur, then cur => good
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def _find(node, pathmax=0):
            if node is None:
                return 0
            
            curValue = 1 if node.val > pathmax else 0
            
            pathmax = max(pathmax, node.val)

            return curValue \
                + _find(node.left, pathmax) \
                + _find(node.right, pathmax)

        return _find(root, root.val)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.diameterOfBinaryTree

