from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomHash = Counter(ransomNote)
        magazineHash = Counter(magazine)
        
        for letter in ransomHash:
            if ransomHash[letter] > magazineHash[letter]:
                return False
            
        return True
    
sol = Solution()
ransomNote = "aa"
magazine = "ab"
print(sol.canConstruct(ransomNote, magazine))