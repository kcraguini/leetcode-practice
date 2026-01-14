class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        match = {"{":"}", "[":"]", "(":")"}

        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack:
                    return False
                previous_opening = stack.pop()
                if match[previous_opening] != c:
                    return False
                
        return not stack

if __name__ == '__main__':
    s = "()[]{}"
    sol = Solution()
    print(f"s: {s} is {sol.isValid(s)}")

    s = "(){{[}}"
    sol = Solution()
    print(f"s: {s} is {sol.isValid(s)}")