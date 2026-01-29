class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
            
        return "".join(stack)
    

if __name__ == '__main__':
    s = "abbaca"
    sol = Solution()
    print(f"After removing duplicates from {s}, we get {sol.removeDuplicates(s)}")

    s = "azxxzy"
    sol = Solution()
    print(f"After removing duplicates from {s}, we get {sol.removeDuplicates(s)}")