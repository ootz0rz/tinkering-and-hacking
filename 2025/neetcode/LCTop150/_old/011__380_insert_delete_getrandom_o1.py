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

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.l = []    

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.map[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.map:
            return False
        
        # save idx and delete from map
        idx = self.map[val]

        # update our list and mapping
        self.l[idx] = self.l[-1] # copy last element to index
        self.map[self.l[idx]] = idx # update idx of this moved element
        
        # cleanup
        self.l.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        randVal = random.randint(0, len(self.l) - 1)
        return self.l[randVal]