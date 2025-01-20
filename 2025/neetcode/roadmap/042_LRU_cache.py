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

# ------------ ListNode
class ListNode:
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev 
    
    def __repr__(self):
        return f"{self.val}"
    
    def __str__(self):
        return self.__repr__()
    
    def __all__(self):
        return f"[{self.prev if self.prev is None else self.prev.__prev__()} << ({self.val}) >> {self.next if self.next is None else self.next.__next__()}]"
    
    def __prev__(self):
        return f"{self.prev if self.prev is None else self.prev.__prev__()} << {self.val}"

    def __next__(self):
        return f"{self.val} >> {self.next if self.next is None else self.next.__next__()}"
# ------------ ListNode

# https://neetcode.io/problems/lru-cache

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity

        self.keyToNode = {}

        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        print(f"### Get[{key}]")
        if not key in self.keyToNode:
            print("No key")
            return -1
        
        node = self.keyToNode[key]
        
        self._send_to_front_of_LL(node)

        print(f"[1] get[{key}]: {self.head.__next__()}")
        
        return node.val

    def put(self, key: int, value: int) -> None:
        print(f"### Put[{key}:{value}]")
        # print(f"[0] put[{key}, {value}]: {self.head.__next__()}")

        # print(f"\t LEN: {len(self.keyToNode)} SIZE LIM: {self.size} NEW KEY?: {(key not in self.keyToNode)}")
        if (len(self.keyToNode) == self.size) and (key not in self.keyToNode):
            # we're at size limit, so gotta remove something else first
            self._remove_lru()

        self._set_or_update_value(key, value)

        print(f"[1] put[{key}, {value}]: {self.head.__next__()}")

    def _set_or_update_value(self, key: int, value: int) -> ListNode:
        print(f"[0] Set or update value[{key}, {value}]: {self.head.__next__()}")

        # new value?
        node = None
        if key not in self.keyToNode:
            node = ListNode(key, value)
            self.keyToNode[key] = node
        else:
            node = self.keyToNode[key]

        # update
        node.value = value

        # place at front
        self._send_to_front_of_LL(node)

        # print(f"[1] Set or update value[{key}, {value}]: {self.head.__next__()}")

        return node
    
    def _send_to_front_of_LL(self, node: ListNode) -> None:
        print(f"[0] send to front[{node}]: {self.head.__next__()}")

        self._remove(node)
        self._add_to_front(node)
    
    def _remove(self, node: ListNode) -> None:
        # remove the node
        tempNext = node.next
        tempPrev = node.prev

        # this might be a new node, and these are null until later updated
        if tempPrev is not None:
            tempPrev.next = tempNext
        
        if tempNext is not None:
            tempNext.prev = tempPrev

    def _add_to_front(self, node: ListNode) -> None:
        tempNext = self.head.next

        self.head.next = node
        tempNext.prev = node

        node.prev = self.head
        node.next = tempNext

    def _remove_lru(self) -> None:
        node = self.tail.prev

        if node == self.head:
            return

        self._remove(node)

        del self.keyToNode[node.key]

        print(f" -> Removed: ", node.__me__())

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.size = capacity

#         self.keyToNode = {}

#         self.head = ListNode()
#         self.tail = ListNode()

#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key: int) -> int:
#         if not key in self.keyToNode:
#             return -1
        
#         node = self.keyToNode[key]
        
#         self._send_to_front_of_LL(node)
        
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         print(f"[0] put[{key}, {value}]: {self.head.__next__()}")

#         print(f"\t LEN: {len(self.keyToNode)} SIZE LIM: {self.size} NEW KEY?: {(key not in self.keyToNode)}")
#         if (len(self.keyToNode) == self.size) and (key not in self.keyToNode):
#             # we're at size limit, so gotta remove something else first
#             self._remove_lru()

#         self._set_or_update_value(key, value)

#         print(f"[1] put[{key}, {value}]: {self.head.__next__()}")

#     def _set_or_update_value(self, key: int, value: int) -> ListNode:
#         print(f"[0] Set or update value[{key}, {value}]: {self.head.__next__()}")

#         # new value?
#         node = None
#         if key not in self.keyToNode:
#             node = ListNode(key, value)
#             self.keyToNode[key] = node
#         else:
#             node = self.keyToNode[key]

#         # update
#         node.value = value

#         # place at front
#         self._send_to_front_of_LL(node)

#         print(f"[1] Set or update value[{key}, {value}]: {self.head.__next__()}")

#         return node
    
#     def _send_to_front_of_LL(self, node: ListNode) -> None:
#         self._remove(node)
#         self._add_to_front(node)
    
#     def _remove(self, node: ListNode) -> None:
#         # remove the node
#         tempNext = node.next
#         tempPrev = node.prev

#         tempPrev.next = tempNext
#         tempNext.prev = tempPrev

#     def _add_to_front(self, node: ListNode) -> None:
#         tempNext = self.head.next

#         self.head.next = node
#         tempNext.prev = node

#         node.prev = self.head
#         node.next = tempNext

#     # def _send_to_front_of_LL(self, node: ListNode) -> None:
#     #     print(f"[0] send to front[{node}]: {self.head.__next__()}")

#     #     # save values for later reference
#     #     oldFirst = self.head.next

#     #     if oldFirst == node:
#     #         print("\t Already first.")
#     #         return

#     #     oldNodePrev = node.prev
#     #     oldNodeNext = node.next

#     #     # fixate node in new position
#     #     node.next = oldFirst
#     #     node.prev = self.head

#     #     # adjust pointers to that node
#     #     self.head.next = node
#     #     oldFirst.prev = node 

#     #     # "heal" space left behind by this node
#     #     # note that when the array is small enough these can be None
#     #     if oldNodePrev is not None:
#     #         oldNodePrev.next = oldNodeNext

#     #     if oldNodeNext is not None:
#     #         oldNodeNext.prev = oldNodePrev

#     #     print(f"[1] send to front[{node}]: {self.head.__next__()}")
#     #     print(f"[2] send to front[{node}]: {self.tail.__prev__()}")

#     def _remove_lru(self) -> None:
#         node = self.tail.prev

#         if node == self.head:
#             return
        
#         tempPrev = node.prev
#         tempNext = node.next

#         tempPrev.next = tempNext
#         tempNext.prev = tempPrev

#         del self.keyToNode[node.key]

#         print(f" -> Removed: ", node)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    # s = LRUCache(2)

    # print("s.put[1,1]", s.put(1, 1))
    # print("s.put[2,2]", s.put(2, 2))
    # print("get[1]", s.get(1))
    # print("s.put[3,3]", s.put(3, 3))
    # print("get[2]", s.get(2))
    # print("s.put[4,4]", s.put(4, 4))
    # print("get[1]", s.get(1))
    # print("get[3]", s.get(3))
    # print("get[4]", s.get(4))

    s = LRUCache(2)
    s.put(1, 10)
    assert s.get(1) == 10
    s.put(2, 20)
    s.put(3, 30)
    assert s.get(2) == 20
    assert s.get(1) == -1
