from typing import List


def compare_maps(m1, m2):
    return m1 == m2


OTHER = "other"


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        global OTHER

        res = []
        pmap = {}
        plen = len(p)

        # count occurances of all letters in p
        for c in p:
            if c in pmap:
                pmap[c] += 1
            else:
                pmap[c] = 1

        smap = {}
        for i, ci in enumerate(s):
            if not (ci in pmap):
                # don't waste space on unimportant characters
                if not (OTHER in smap):
                    smap[OTHER] = 0

                smap[OTHER] = smap[OTHER] + 1
            else:
                # count other chars
                if not (ci in smap):
                    smap[ci] = 0

                smap[ci] += 1

            if i >= plen:
                old_char = s[i - plen]

                if not (old_char in pmap):
                    old_char = OTHER

                if smap[old_char] == 1:
                    del smap[old_char]
                else:
                    smap[old_char] -= 1

            if compare_maps(smap, pmap):
                res.append(i - plen + 1)

        return res


if __name__ == "__main__":
    sol = Solution()

    def checkSolution(s, p, expected, msg="Expected `{0}` but got `{1}`"):
        r = sol.findAnagrams(s, p)
        assert r == expected, msg.format(expected, r)

    checkSolution(s="cbaebabacd", p="abc", expected=[0, 6])

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
