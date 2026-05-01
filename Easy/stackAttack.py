class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        stack = []

        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                prev = stack.pop()
                if c != valid[prev]:
                    return False
                
        return True
    
s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("[([{}])]"))
print(s.isValid("[{]}"))