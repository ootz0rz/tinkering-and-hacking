# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4514/

import pprint
from typing import List, Optional, Dict

# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from TestHarness import *

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# ------------- STACKS -------------
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/simplify-path/description/
# ----------------------------------------------------------------------------------------------------------------------


def simplifyPath(path: str) -> str:
    out = []

    def _process_buff(b):
        nonlocal out

        if len(b) == 0:
            return

        if b == "..":
            if len(out) > 0:
                out.pop()
        elif b == ".":
            return
        else:
            out.append(b)

    buff = ""
    for c in path:
        # print(c, "-", buff, "-", out)

        if c == "/":
            _process_buff(buff)
            buff = ""
        else:
            buff = buff + c

    _process_buff(buff)

    return "/" + "/".join(out)


"""
# given
check_solution_simple(simplifyPath, args=["/home/"], expected="/home")
check_solution_simple(simplifyPath, args=["/../"], expected="/")
check_solution_simple(simplifyPath, args=["/home//foo/"], expected="/home/foo")
check_solution_simple(simplifyPath, args=["/a//b////c/d//././/.."], expected="/a/b/c")
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/make-the-string-great/description/
# ----------------------------------------------------------------------------------------------------------------------


def makeGood(s: str) -> str:
    buf = []

    for c in s:
        if len(buf) > 0:
            if (buf[-1] != c) and (buf[-1].lower() == c.lower()):
                buf.pop()
                continue

        buf.append(c)

    return "".join(buf)


"""
# given
check_solution_simple(makeGood, args=["s"], expected="s")
check_solution_simple(makeGood, args=["leEeetcode"], expected="leetcode")
check_solution_simple(makeGood, args=["abBAcC"], expected="")
"""

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# ------------- QUEUE -------------
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/moving-average-from-data-stream/description/
# ----------------------------------------------------------------------------------------------------------------------


class MovingAverage:
    def __init__(self, size: int):
        from collections import deque

        self.window = size
        self.q = deque()

    def next(self, val: int) -> float:
        self.q.append(val)

        if len(self.q) > self.window:
            self.q.popleft()

        avg = 0
        for v in self.q:
            avg = avg + v

        return avg / len(self.q)


"""
# given
movingAverage = MovingAverage(3)
print(movingAverage.next(1))
print(movingAverage.next(10))
print(movingAverage.next(3))
print(movingAverage.next(5))
"""

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# ------------- MONOTONIC STUFF -------------
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/next-greater-element-i/description/
# ----------------------------------------------------------------------------------------------------------------------

"""
496. Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""

# nums1 = m
# nums2 = n
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Idea:

    Build a monotonic increasing Q of nums2, from back to front
    """
    from collections import defaultdict, deque

    ans = []

    # build dict for nums1, used to look up to see if we're a query number
    # while building the DQ, but also to store answers as they're found
    dn1 = defaultdict(int)
    for n in nums1:
        dn1[n] = -1

    """
    We take O(m) space for dn1, O(m) to process this
    """

    # generate deque with largest to the right of index, and extract answers
    dq = deque()
    j = len(nums2) - 1
    while j >= 0:
        cnum = nums2[j]

        # check if we need to start removing elements from dq... basically we only
        # want to keep elements in our DQ that are larger than the current number
        while len(dq) > 0 and cnum >= dq[0]:
            dq.popleft()

        # if we encounter a number which matches a query, save the answer here
        if cnum in dn1:
            if len(dq) > 0:
                dn1[cnum] = dq[0]

        # store to the left... everything in the DQ should be larger than us, if there
        # is anything at all
        dq.appendleft(cnum)

        j = j - 1

    """
    O(n) space for dq, and we take O(n) time to process and generate it
    """

    # collect all answers into our final array
    for n in nums1:
        ans.append(dn1[n])

    """
    O(m) runtime again, and O(m) more space for answers array
    """

    return ans
    """
    SPACE: O(m+n+m) but m is strictly <= n, so O(3n) => O(n)
    TIME: same as above => O(n)
    """


"""
# given
check_solution_simple(
    nextGreaterElement, args=[[4, 1, 2], [1, 3, 4, 2]], expected=[-1, 3, -1]
)
check_solution_simple(nextGreaterElement, args=[[2, 4], [1, 2, 3, 4]], expected=[3, -1])
"""
