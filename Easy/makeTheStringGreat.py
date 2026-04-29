class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        n = len(s)
        for i in range(n): 
            if stack and s[i].isupper() or stack and stack[-1].isupper():
                stack.pop()
            else:
                stack.append(s[i])
            print(stack)
                
        return "".join(stack)


solution = Solution()
print(solution.makeGood("leEeetcode"))
