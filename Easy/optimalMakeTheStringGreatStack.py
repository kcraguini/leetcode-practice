class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for curr_char in s:
            if stack and abs(ord(stack[-1]) - ord(curr_char)) == 32:
                stack.pop()
            else:
                stack.append(curr_char)

        return ''.join(stack)
    
if __name__ == '__main__':
    sol = Solution()
    s = "leEeetcode"
    print(sol.makeGood(s))  # Output: "leetcode"
    sol = Solution()
    s = "abBAcCd"
    print(sol.makeGood(s))  # Output: "d"        