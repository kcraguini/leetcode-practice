from typing import List

class Solution:
    def repeatedChar(self, s: str) -> str:
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
               return s[i]
            else:
                seen.add(s[i])


s = Solution()
print(s.repeatedChar("abccbaacz"))