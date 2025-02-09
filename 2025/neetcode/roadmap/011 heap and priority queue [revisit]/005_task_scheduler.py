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

# https://neetcode.io/problems/task-scheduling

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # build freq map
        tFreq = {}

        for t in tasks:
            if not t in tFreq:
                tFreq[t] = 0

            tFreq[t] += 1

        print(f"freqs: {tFreq}")

        # we then build a max-heap by frequency
        mh = [] # -frequency, letter
        heapq.heapify(mh)
        for letter in tFreq:
            heapq.heappush(mh, (-tFreq[letter], letter))
        
        print(f"heap: {mh}")

        # we set aside a queue to use for timeouts
        # note that a Q works here because subsequent elements will 
        # ALWAYS have a higher (time until exectuion) than the previous element,
        # since we process one tick at a time
        timers = deque() # letter, freq, time

        # and now we start processing, one tick at a time,
        # until we have no tasks and timers left
        time = 0
        while len(mh) > 0 or len(timers) > 0:
            time = time + 1

            print(f"Time Step: {time}")
            
            # check if we have any items in queue to process
            print(f"\tCheck Timer Queue: {timers}")
            while len(timers) > 0 and timers[0][2] == time:
                l, f, t = timers.popleft()

                print(f"\t\t -> Add to heap from queue: {l}:{f} at T[{time}]={t}")
                heapq.heappush(mh, (f, l))

            # process the first element in heap, if we have any
            if len(mh) == 0:
                print(f"\tSkip heap: {mh}")
                continue

            print(f"\tCheck heap: {mh}")
            freq, letter = heapq.heappop(mh)
            freq *= -1

            print(f"\t\t Process from heap: {letter}:{freq}")
            if freq > 1:
                # add to queue 
                print(f"\t\t -> Add to queue: {letter}:{(freq - 1)}:{(time + n + 1)}")
                timers.append((letter, -(freq - 1), time + n + 1))
        
        return time

        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.leastInterval

    check_solution_simple(  
        sf,
        args=[["X","X","Y","Y"], 2],
        expected=5
    )