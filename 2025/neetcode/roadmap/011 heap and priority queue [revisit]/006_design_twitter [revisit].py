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

# https://neetcode.io/problems/design-twitter-feed

class Twitter:
    __FEED_LIM = 10

    def __init__(self):
        self.user_data = defaultdict(list) # (time, tweetid)

        self.follows = defaultdict(set) # userid -> [userIds followed]

        self.timeCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.user_data:
            self.user_data[userId] = []

        self.user_data[userId].append((self.timeCount, tweetId))
        self.timeCount -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = [] # (time, tweetid, followed user, 'next' index in their posts)
        
        # we treat a user as following themselves by default to simplify below
        self.follow(userId, userId)

        # init the minheap with each of our followed users
        for u in self.follows[userId]:
            
            if not u in self.user_data:
                continue

            # get the last element in their posts
            n = len(self.user_data[u]) - 1
            time, tweetid = self.user_data[u][n]

            # add to our minHeap
            # minHeap.append((time, tweetid, u, n - 1))
            heapq.heappush(minHeap, (time, tweetid, u, n - 1))

        # now we begin processing the heap
        # heapq.heapify(minHeap)

        while len(minHeap) > 0 and len(res) < self.__FEED_LIM:
            # pop most recent from heap to add to result
            time, tweetid, user, index = heapq.heappop(minHeap)
            res.append(tweetid)

            # add more from the user we just processed if they have any, to our heap
            if index >= 0:
                t, tid = self.user_data[user][index]
                heapq.heappush(minHeap, (t, tid, user, index - 1))

        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    t = Twitter()

    t.postTweet(1, 10)
    t.postTweet(2, 20)

    check_solution_simple(t.getNewsFeed, args=[1], expected=[10])
    check_solution_simple(t.getNewsFeed, args=[2], expected=[20])

    t.follow(1, 2)

    check_solution_simple(t.getNewsFeed, args=[1], expected=[20, 10])
    check_solution_simple(t.getNewsFeed, args=[2], expected=[20])

    t.unfollow(1, 2)

    check_solution_simple(t.getNewsFeed, args=[1], expected=[10])