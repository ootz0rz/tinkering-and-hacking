# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4511/

import pprint
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

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/subarray-sum-equals-k/
# ----------------------------------------------------------------------------------------------------------------------


def subarraySum(nums: List[int], k: int) -> int:
    from collections import defaultdict

    # declare hashmap, default dict of int gives us niceties when a key doesn't exist (ex: auto add when setting value,
    # or returning 0 when accessing value that doesn't exist)
    counts = defaultdict(int)
    counts[0] = 1  # init empty set

    ans = 0
    curr = 0

    for n in nums:
        curr += n

        cons = curr - k
        if cons in counts:
            ans += counts[cons]

        counts[curr] = counts[curr] + 1

    return ans


# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/count-number-of-nice-subarrays/
# ----------------------------------------------------------------------------------------------------------------------
def numberOfSubarrays(nums: List[int], k: int) -> int:
    from collections import defaultdict

    counts = defaultdict(int)
    counts[0] = 1  # init empty set

    ans = 0
    curr = 0

    for n in nums:
        if n % 2 == 1:
            curr += 1  # num odd so far

        cons = curr - k
        if cons in counts:
            ans += counts[cons]

        counts[curr] = counts[curr] + 1

    return ans


"""
# given
check_solution_simple(numberOfSubarrays, args=[[1, 1, 2, 1, 1], 3], expected=2)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
# ----------------------------------------------------------------------------------------------------------------------
def findWinners(matches: List[List[int]]) -> List[List[int]]:
    from collections import defaultdict

    num_losses = defaultdict(int)

    for winner, loser in matches:
        num_losses[winner] = num_losses[winner]
        num_losses[loser] = num_losses[loser] + 1

    players = sorted(num_losses.keys())

    ans = [[], []]
    for p in players:
        if num_losses[p] == 0:
            ans[0].append(p)
        elif num_losses[p] == 1:
            ans[1].append(p)

    return ans


"""
# given
check_solution_simple(
    findWinners,
    args=[
        [
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    ],
    expected=[[1, 2, 10], [4, 5, 7, 8]],
)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/largest-unique-number/description/
# ----------------------------------------------------------------------------------------------------------------------


def largestUniqueNumber(nums: List[int]) -> int:
    from collections import defaultdict

    counts = defaultdict(int)

    for n in nums:
        counts[n] = counts[n] + 1

    ans = -1
    for k in counts.keys():
        if counts[k] == 1:
            ans = max(ans, k)

    return ans


"""
# given
check_solution_simple(
    largestUniqueNumber, args=[[5, 7, 3, 9, 4, 9, 8, 3, 1]], expected=8
)
check_solution_simple(largestUniqueNumber, args=[[9, 9, 8, 8]], expected=-1)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/maximum-number-of-balloons/description/
# ----------------------------------------------------------------------------------------------------------------------


__BALLOON__ = {
    "b": 1,
    "a": 1,
    "l": 2,
    "o": 2,
    "n": 1,
}


def maxNumberOfBalloons(text: str) -> int:
    from collections import defaultdict

    currcount = defaultdict(int)
    bk = __BALLOON__.keys()
    for t in text:
        if t in bk:
            currcount[t] += 1

    ans = 99999999  # big enough since gauranteed 10^4 chars in text at most
    for k in bk:
        if not (k in currcount):
            return 0

        ans = min(ans, currcount[k] // __BALLOON__[k])

    return ans


"""
#given
check_solution_simple(maxNumberOfBalloons, args=["nlaebolko"], expected=1)
check_solution_simple(maxNumberOfBalloons, args=["loonbalxballpoon"], expected=2)
check_solution_simple(maxNumberOfBalloons, args=["leetcode"], expected=0)
check_solution_simple(maxNumberOfBalloons, args=["baoollnnololgbax"], expected=2)
check_solution_simple(
    maxNumberOfBalloons,
    args=[
        "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    ],
    expected=10,
)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/ransom-note/description/
# ----------------------------------------------------------------------------------------------------------------------


def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import defaultdict

    counts = defaultdict(int)

    if len(magazine) < len(ransomNote):
        return False

    for c in magazine:
        counts[c] = counts[c] + 1

    for r in ransomNote:
        if (r not in counts) or (counts[r] == 0):
            return False
        else:
            counts[r] = counts[r] - 1

    return True


"""
#given
check_solution_simple(canConstruct, args=["a", "b"], expected=False)
check_solution_simple(canConstruct, args=["aa", "ab"], expected=False)
check_solution_simple(canConstruct, args=["aa", "aab"], expected=True)

#me
check_solution_simple(canConstruct, args=["aaa", "aa"], expected=False)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# ----------------------------------------------------------------------------------------------------------------------


def lengthOfLongestSubstring_old(s: str) -> int:
    from collections import defaultdict

    left = right = ans = cur = 0

    c = defaultdict(int)

    while left <= right and right < len(s):
        c[left] = c[left] + 1
        cur = cur + 1

        while c[right] > 1 and left <= right:
            c[left] = c[left] - 1
            if c[left] == 0:
                del c[left]

            cur = cur - 1
            left = left + 1

        ans = max(ans, cur)

        right = right + 1

    return ans


def lengthOfLongestSubstring(s: str) -> int:
    from collections import defaultdict

    left = ans = cur = 0

    c = defaultdict(int)

    for ridx in range(len(s)):
        c[s[ridx]] += 1

        cur = cur + 1

        while c[s[ridx]] >= 2:
            c[s[left]] -= 1
            if c[s[left]] == 0:
                del c[s[left]]

            left = left + 1

            cur = cur - 1

        ans = max(ans, cur)

    return ans


check_solution_simple(lengthOfLongestSubstring, args=["abcabcbb"], expected=3)
check_solution_simple(lengthOfLongestSubstring, args=["bbbbb"], expected=1)
check_solution_simple(lengthOfLongestSubstring, args=["pwwkew"], expected=3)
