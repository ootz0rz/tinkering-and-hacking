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

# https://leetcode.com/problems/word-search-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass
        


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
