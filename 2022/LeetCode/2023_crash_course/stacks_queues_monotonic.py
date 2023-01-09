# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4514/

import pprint
from typing import List, Optional, Dict

# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from TestHarness import *

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
