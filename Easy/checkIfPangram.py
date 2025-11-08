from typing import List

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

s = Solution()
phrase = "thequickbrownfoxjumpsoverthelazydog"
print(s.checkIfPangram(phrase))

phrase2 = "leetcode"
print(s.checkIfPangram(phrase2))