from typing import List
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

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

        An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
        '''
        if len(s) != len(t):
            return False

        off = ord('a')

        l = [0] * 26 # const letter range

        i = 0
        while i < len(s):
            io = ord(s[i]) - off
            to = ord(t[i]) - off

            l[io] += 1
            l[to] -= 1
            # if same number of letters, each idx should be 0 by end
            
            i = i + 1

        for e in l:
            if e != 0:
                return False
        
        return True
        
            

if __name__ == '__main__':
    s = Solution().isAnagram

    assert s("", "") == True

    assert s("a", "a") == True
    assert s("a", "b") == False

    assert s("aa", "aa") == True
    assert s("aaa", "aaa") == True

    assert s("aa", "ab") == False
    assert s("ba", "aa") == False

    assert s("aaa", "aba") == False
    assert s("aba", "aaa") == False
    assert s("bab", "aab") == False

    assert s("racecar", "carrace") == True
    assert s("jar", "jam") == False