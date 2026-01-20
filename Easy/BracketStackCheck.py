class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {
            "{" : "}",
            "[" : "]",
            "(" : ")"        
        }
        
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if not stack:
                    return False

                previous_bracket = stack.pop()
                if mapping[previous_bracket] != c:
                    return False
        
        return not stack


if __name__ == "__main__":
    test_strings = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    sol = Solution()
    for s in test_strings:
        print(f"{s}: {sol.isValid(s)}")