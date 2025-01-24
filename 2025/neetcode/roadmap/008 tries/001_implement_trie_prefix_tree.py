from typing import List, Optional, Self
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

# https://neetcode.io/problems/implement-prefix-tree

class TrieNode:
    def __init__(self, value: str, isEnd: bool=False):
        self.val = value
        self.isEnd = isEnd
        self.children = {} # val -> TrieNode

    def contains(self, value: str) -> bool:
        return value in self.children

    def add_child(self, childVal: str, isEnd: Optional[bool]=False) -> Self:
        if childVal in self.children:
            # if a child with this val already exists, all we
            # care about here is if this child should be marked
            # as a possible word-end
            self.children[childVal].isEnd |= isEnd
        else:
            self.children[childVal] = TrieNode(childVal, isEnd)
        
        return self.children[childVal]        
    
    def __str__(self):
        return f"<{self.val}:{self.isEnd}:[{self.children}]>"
    
    def __repr__(self):
        return f"[[ {self.isEnd}:{self.children} ]]"
        
class PrefixTree:

    def __init__(self):
        self.root = TrieNode("ROOT")

    def insert(self, word: str) -> None:
        node = self.root
        for idx, e in enumerate(word):
            lastLetter = (idx == (len(word) - 1))
            node = node.add_child(childVal=e, isEnd=lastLetter)

    def search(self, word: str) -> bool:
        node = self.root
        for idx, e in enumerate(word):
            if not node.contains(e):
                return False
            
            node = node.children[e]
            
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for idx, e in enumerate(prefix):
            if not node.contains(e):
                return False
            
            node = node.children[e]
            
        return True
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = PrefixTree()
    
    print(f"p do: {s.startsWith('do')}")

    s.insert("dog")
    print(s.root)

    s.insert("dock")
    print(s.root)

    print(f"do: {s.search('do')}")
    print(f"p do: {s.startsWith('do')}")

    s.insert("do")
    print(s.root)

    print(f"do: {s.search('do')}")

    print(f"dog: {s.search('dog')}")

    print(f"dock: {s.search('dock')}")

    print(f"dogs: {s.search('dogs')}")

    print(f"doggy: {s.search('doggy')}")

    print(f"p dog: {s.startsWith('dog')}")
    print(f"p doggy: {s.startsWith('doggy')}")
    print(f"p sub: {s.startsWith('sub')}")