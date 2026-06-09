class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        # check if even
        if len(s) % 2 != 0: 
            return False
        
        for char in s:
            # if closed then pop
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        return True if not stack else False

        

        