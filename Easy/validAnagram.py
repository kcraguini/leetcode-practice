from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCnt = Counter(s)
        tCnt = Counter(t)

        return sCnt == tCnt
    
sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))