class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        match = {"{":"}", "[":"]", "(":")"}

        for c in s:
            if c in match:
                stack.append(c)
            else:
                print(f"Not in the stack {c}")
                if not stack: # If the stack is empty automatically false
                    return False
                
                else:
                    prev_matching = stack.pop()
                    if match[prev_matching] != c:
                        return False
                    
        return True
if __name__ == '__main__':
    s = "()[]{}"
    sol = Solution()
    print(f"s: {s} is {sol.isValid(s)}")

    s = "(){{[}}"
    sol = Solution()
    print(f"s: {s} is {sol.isValid(s)}")