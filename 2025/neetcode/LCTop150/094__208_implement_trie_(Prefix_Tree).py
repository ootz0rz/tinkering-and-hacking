from typing import List, Optional, Self, Set, Dict
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

# https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150

class TNode:
    def __init__(self, val:str=""):
        self.value: str = val
        self.children = {} # char: Node
        self.isTerminator: bool = False

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return f"<{self.value}, {self.isTerminator}, ::{self.children}::>"

class Trie:

    def __init__(self):
        self.root = TNode()

    def insert(self, word: str) -> None:
        n = self.root

        for c in word:
            if not c in n.children:
                t = TNode(c)
                n.children[c] = t
            n = n.children[c]
        
        n.isTerminator = True
        
        # print(f"Insert: {word} => {self.root}")

    def search(self, word: str) -> bool:
        n = self.root

        for c in word:
            if not c in n.children:
                return False
            n = n.children[c]

        return n.isTerminator

    def startsWith(self, prefix: str) -> bool:
        n = self.root 

        for c in prefix:
            if not c in n.children:
                return False
            n = n.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Trie()
    s.insert("cat")
    print(s.search("cat"))
    print(s.search("car"))
    s.insert("car")
    print(s.search("car"))
    print(s.search("cam"))
    print(s.search("cat"))
    print()
    print(s.startsWith("c"))
    print(s.startsWith("ca"))
    print(s.startsWith("car"))
    print(s.startsWith("cat"))
    print(s.startsWith("catch"))
    print(s.startsWith("gat"))


    # s = Solution()
    # sf = s.ladderLength

    # check_solution_simple(  
    #     sf,
    #     args=["hit", "cog", ["hot","dot","dog","lot","log"]],
    #     expected=0
    # )

    # check_solution_simple(  
    #     sf,
    #     args=["hit", "cog", ["hot","dot","dog","lot","log","cog"]],
    #     expected=5
    # )
