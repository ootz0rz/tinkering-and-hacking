# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4511/

from typing import List, Optional, Dict

# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from TestHarness import *

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/two-sum/
# ----------------------------------------------------------------------------------------------------------------------


def twoSum(nums: List[int], target: int) -> List[int]:
    m = {}

    for idx, n in enumerate(nums):
        remainder = target - n

        if remainder in m:
            return [m[remainder], idx]

        m[n] = idx

    return [-1, -1]


"""
# given
check_solution_simple(twoSum, args=[[2, 7, 11, 15], 9], expected=[0, 1])


check_solution_simple(twoSum, args=[[0, 0], 0], expected=[0, 1])
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
# ----------------------------------------------------------------------------------------------------------------------

__NUM_LET__ = 26


def checkIfPangram(sentence: str) -> bool:
    s = set()

    for c in sentence:
        s.add(c)

        if len(s) == __NUM_LET__:
            return True

    return False


"""
# given
check_solution_simple(
    checkIfPangram, args=["thequickbrownfoxjumpsoverthelazydog"], expected=True
)

check_solution_simple(checkIfPangram, args=[""], expected=False)
check_solution_simple(checkIfPangram, args=["a"], expected=False)
check_solution_simple(
    checkIfPangram, args=["abcdefghijklmnopqrstuvwxyz"], expected=True
)
check_solution_simple(
    checkIfPangram, args=["abcdefghijklmnopqrstuvwxy"], expected=False
)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/missing-number/description/
# ----------------------------------------------------------------------------------------------------------------------


def missingNumber(nums: List[int]) -> int:
    n = len(nums)

    sum = 0
    for e in nums:
        sum = sum + e

    return int((((n + 1) * (0 + n)) / 2) - sum)


"""
# given
check_solution_simple(missingNumber, args=[[3, 0, 1]], expected=2)
check_solution_simple(missingNumber, args=[[0, 1]], expected=2)
check_solution_simple(missingNumber, args=[[9, 6, 4, 2, 3, 5, 7, 0, 1]], expected=8)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/counting-elements/description/
# ----------------------------------------------------------------------------------------------------------------------


def countElements(arr: List[int]) -> int:
    s = set(arr)

    count = 0

    for e in arr:
        if (e + 1) in s:
            count = count + 1

    # 2 pass, O(2N) -> O(N)

    return count


"""
# given
check_solution_simple(countElements, args=[[1, 2, 3]], expected=2)

check_solution_simple(countElements, args=[[1, 1, 3, 3, 5, 5, 7, 7]], expected=0)
"""
