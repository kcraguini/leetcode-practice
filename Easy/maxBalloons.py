from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashText = Counter(text)
        balloonHash = Counter("balloon")
        
        cnt = float("inf")      
        
        for c in balloonHash:
            quotient = int(hashText[c] / balloonHash[c])
            cnt = min(quotient, cnt)
            
        return cnt
    
sol = Solution()
text = "loonbalxballpoon"
print(sol.maxNumberOfBalloons(text))