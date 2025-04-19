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

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

'''
Idea:

We're given the target as a node inside the tree at root

We can search from root -> target, and track our path and build info that lets us go from a child -> parent along the way

Once we find target, then its BFS to k
'''
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        pMap = {None: None} # child -> parent

        def findTarget(node):
            nonlocal target

            if node is None:
                return

            if node == target:
                return 
            
            if node.left:
                pMap[node.left] = node
                findTarget(node.left)
            
            if node.right:
                pMap[node.right] = node
                findTarget(node.right)
        
        findTarget(root)

        # now we can just bfs from the target outwards
        q = deque([(target, 0)])
        v = set()

        res = []
        while len(q) > 0:
            #print(f"Q: {q} -- V: {v}")

            node, dist = q.popleft()

            #print(f" -> POP {node}, {dist} from Q")

            if node in v:
                continue

            if dist == k:
                #print(f"\t => Adding node: {node} with dist: {dist}=={k}, q: {q} -- v: {v}")
                res.append(node.val)
                continue

            v.add(node)
            
            if dist > k:
                continue
            
            if node.left:
                q.append((node.left, dist + 1))
            
            if node.right:
                q.append((node.right, dist + 1))

            if node in pMap:
                q.append((pMap[node], dist + 1))
            
        return res

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.distanceK

    root = GEN_TREE_FROM_LIST([3,5,1,6,2,0,8,null,null,7,4])

    check_solution_as_sets(
        sf,
        args=[root, root.left, 2],
        expected=[7,4,1],
    )