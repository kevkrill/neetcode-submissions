class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join([c.lower() for c in s if c.isalnum()])
        
        i = 0 
        k = len(s)-1

        while i <= k:
            if s[i] == s[k]:
                i += 1
                k -= 1
            else:
                return False
        

        return True