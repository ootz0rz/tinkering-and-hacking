valMap = {
    'I' : 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

subSets = {
    'I' : set(["V", "X"]),
    'X' : set(["L", "C"]),
    'C' : set(["D", "M"]),
}

class Solution:
    def romanToInt(self, s: str) -> int:
        
        i = 0
        total = 0
        while i < len(s):
            e = s[i]

            if (e in subSets) and (i < len(s) - 1) and s[i+1] in subSets[e]:
                total += valMap[s[i+1]] - valMap[e]
                i += 1
            else:
                total += valMap[e]

            #print(f"e: {e} -> total: {total}")

            i += 1

        return total
    
s = Solution()
s.romanToInt("MCMXCIV")