from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnts = defaultdict(int)
        
        left = ans = cnt = 0
        
        for right in range(len(s)):
            cnts[s[right]] += 1
            cnt += 1
            
            while cnt > len(cnts):
                cnts[s[left]] -= 1
                cnt -= 1
                if cnts[s[left]] == 0:
                    del cnts[s[left]]
                    
                left += 1
            ans = max(ans, cnt)
            
        return ans
            
sol = Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))