class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        # 2ptr from each side
        while i < j:
            # skip left until alphanum found
            while not s[i].isalnum() and i < j:
                i += 1
            
            # skip right until alphanum found
            while not s[j].isalnum() and i < j:
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        
        return True