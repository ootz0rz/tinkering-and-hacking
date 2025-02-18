class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        tidx = 0
        sidx = 0

        while tidx < len(t) and sidx < len(s):
            #print(f"tidx: {tidx} < lt:{len(t)} <{t[tidx]}> and sidx: {sidx} < ls:{len(s)} <{s[sidx]}>")

            if t[tidx] != s[sidx]:
                tidx += 1
                continue

            sidx += 1
            tidx += 1

        #print(f"s: {sidx} t: {tidx} | sl: {len(s)} tl: {len(t)}")

        return sidx <= tidx and sidx == len(s)

s = Solution()
print(s.isSubsequence("abc", "ajjbjjjcoo"))