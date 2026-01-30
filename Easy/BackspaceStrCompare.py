class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stringBuilder(string):
            stack = []

            for character in string:
                if character == '#':
                    if stack:
                        stack.pop()

                else:
                    stack.append(character)
            return "".join(stack)

        return stringBuilder(s) == stringBuilder(t)
    

if __name__ == '__main__':
    sol = Solution()

    s = "ab#c"
    t = "ad#c"

    print(sol.backspaceCompare(s, t))

    s = "y#fo##f"
    t = "y#f#o##f"

    print(sol.backspaceCompare(s, t))