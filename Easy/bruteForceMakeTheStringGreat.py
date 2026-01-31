class Solution:
    def makeGood(self, s: str) -> str:
        

        stack = []
        for c in s:
            if stack and stack[-1].upper() == c.upper():
                if stack[-1].isupper() and c.islower() or stack[-1].islower() and c.isupper():
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return "".join(stack)


if __name__ == '__main__':
    sol = Solution()

    s = "leEeetcode"
    print(f"The good string for {s} is {sol.makeGood(s)}")

    s = "abBAcC"
    print(f"The good string for {s} is {sol.makeGood(s)}")

    s = "s"
    print(f"The good string for {s} is {sol.makeGood(s)}")