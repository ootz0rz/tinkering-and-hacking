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

# https://leetcode.com/problems/word-ladder/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # # first just check if this is a valid path
        # wordSet = set(wordList)
        # if not endWord in wordSet:
        #     return 0

        L = len(wordList[0])
        
        # we want to do some amount of processing on wordlist to understand which words are 1-dist
        # away from each other
        wMap = defaultdict(set)
        for word in wordList:
            # we generate an intermediate representation of each word, replacing one letter at a
            # time with *
            #
            # by the time we finish the outerloop, we'll have all words that can have only that
            # letter changed grouped together
            # 
            # Ex: dog, dot, lot => {do*:[dog, dot], *ot:[dot, lot]}
            for idx in range(len(word)):
                nword = word[:idx] + "*" + word[idx + 1:]
                wMap[nword].add(word)
        
        print(f"Generated wMap: {wMap}")
        
        # BFS from start -> end can get crazy per level... to reduce the width of the solution
        # we can do BFS starting from both ends and have them continue until they find a common
        # node which gives us our path
        qf = deque([(beginWord, 0)])
        qb = deque([(endWord, 0)])

        vf = {} # {word: dist, ...}
        vb = {}

        while len(qf) > 0 and len(qb) > 0:
            print(f"Process front:<{qf}> and back:<{qb}>")
            # process each set one level at a time
            for _ in range(len(qf)):
                node = qf.popleft()
                nf, dist = node

                if nf in vf:
                    # already visited
                    continue 

                if nf in vb:
                    # whooo, match!
                    return dist + vb[nf]
                
                vf[nf] = dist

                # go to neighbours
                used = set([])
                for idx in range(len(nf)):
                    nword = nf[:idx] + "*" + nf[idx + 1:]

                    if nword in used:
                        continue
                    
                    used.add(nword)
                    for neigh in wMap[nword]:
                        qf.append((neigh, dist + 1))
                print(f"\t => [0] Generated new neighbours: {len(qf)} -- visited: {vf}")
            
            for _ in range(len(qb)):
                node = qb.popleft()
                nb, dist = node

                if nb in vb:
                    continue

                if nb in vf:
                    return dist + vf[nb]
                
                vb[nb] = dist

                # go to neighbours
                used = set([])
                for idx in range(len(nb)):
                    nword = nb[:idx] + "*" + nb[idx + 1:]

                    if nword in used:
                        continue
                    
                    used.add(nword)
                    
                    for neigh in wMap[nword]:
                        qb.append((neigh, dist + 1))
                print(f"\t => [1] Generated new neighbours: {len(qb)} -- visited: {vb}")
        
        return -1


from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.length: int = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict: Dict[str, List[str]] = defaultdict(list)

    def visitWordNode(
        self,
        queue: Deque[str],
        visited: Dict[str, int],
        others_visited: Dict[str, int],
    ) -> Any:
        queue_size: int = len(queue)
        for _ in range(queue_size):
            current_word: str = queue.popleft()
            for i in range(self.length):
                # Intermediate words for current word
                intermediate_word: str = (
                    current_word[:i] + "*" + current_word[i + 1 :]
                )

                # Next states are all the words which share the same intermediate state.
                for word in self.all_combo_dict[intermediate_word]:
                    # If the intermediate state/word has already been visited from the
                    # other parallel traversal this means we have found the answer.
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        # Save the level as the value of the dictionary, to save number of hops.
                        visited[word] = visited[current_word] + 1
                        queue.append(word)

        return None

    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        # Queues for birdirectional BFS
        queue_begin: Deque[str] = collections.deque(
            [beginWord]
        )  # BFS starting from beginWord
        queue_end: Deque[str] = collections.deque(
            [endWord]
        )  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin: Dict[str, int] = {beginWord: 1}
        visited_end: Dict[str, int] = {endWord: 1}
        ans: Any = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(
                    queue_begin, visited_begin, visited_end
                )
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.ladderLength

    check_solution_simple(  
        sf,
        args=["hit", "cog", ["hot","dot","dog","lot","log"]],
        expected=0
    )

    check_solution_simple(  
        sf,
        args=["hit", "cog", ["hot","dot","dog","lot","log","cog"]],
        expected=5
    )
