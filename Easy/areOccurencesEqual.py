from typing import List
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s:str) -> bool:
        return len(set(Counter(s).values())) == 1

sol = Solution()
#s = "abacbc"
s = "aaabsdmfklmlamklkdkkdkskkallvllsldfaoosbbaab"
print(sol.areOccurrencesEqual(s)) 