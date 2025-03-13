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
        return self.__to_str__(True)
    
    def __to_str__(self, children=False):
        return f"{self.value}, T:{self.isTerminator}{' ['+str(self.children)+']' if children and len(self.children) > 0 else ''}"

class WordDictionary:

    def __init__(self):
        self.root = TNode()

    def addWord(self, word: str) -> None:
        n = self.root

        for c in word:
            if not c in n.children:
                t = TNode(c)
                n.children[c] = t
            n = n.children[c]
        
        n.isTerminator = True

        #print(f"Add Word: <{word}> => {self.root}")
        
    def search(self, word: str) -> bool:
        q = deque([self.root])

        for idx, c in enumerate(word):
            #print(f"Search Loop c[{idx}]={c} in {word}, q: {[n.__to_str__() for n in q]}")

            if len(q) == 0:
                # we've run out of things to check, so probably our search term is longer than longest word we've got
                #print(f"\t ==> Word too long?")
                return False

            # Wildcard? add the children of all the current Q for next step
            if c == '.':
                for _ in range(len(q)):
                    n = q.popleft()
                    q.extend(n.children.values())
                #print(f"\twild card, added children: {[n.__to_str__() for n in q]}")
            else:
                # Check for c in the children of the current Q level
                found = False
                for _ in range(len(q)):
                    n = q.popleft()

                    if not c in n.children:
                        continue

                    # add the child we found to next iteration and mark as we found at least one
                    # NOTE we could probably also just check length of Q after we finish
                    found = True
                    q.append(n.children[c])
                #print(f"\tnormal check, found? {found}, Q: {[n.__to_str__() for n in q]}")
        
        # finally, check for terminator
        while len(q) > 0:
            n = q.popleft()
            if n.isTerminator:
                return True
        
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

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

    s = WordDictionary()
    s.addWord("bra")
    s.addWord("bad")
    s.addWord("dad")
    s.addWord("mad")
    w="pad"; print(f"{w}: ", s.search(w))
    w="bad"; print(f"{w}: ", s.search(w))
    w=".ad"; print(f"{w}: ", s.search(w))
    w="b.."; print(f"{w}: ", s.search(w))

    # s = Trie()
    # s.insert("cat")
    # print(s.search("cat"))
    # print(s.search("car"))
    # s.insert("car")
    # print(s.search("car"))
    # print(s.search("cam"))
    # print(s.search("cat"))
    # print()
    # print(s.startsWith("c"))
    # print(s.startsWith("ca"))
    # print(s.startsWith("car"))
    # print(s.startsWith("cat"))
    # print(s.startsWith("catch"))
    # print(s.startsWith("gat"))


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
