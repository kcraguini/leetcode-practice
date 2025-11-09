from collections import defaultdict

class Solution:
    def find_longest_substring(self, s: str, k: int) -> int:
        cnts = defaultdict(int)
        left = ans = 0 
        for right in range(len(s)):
            cnts[s[right]] += 1
            while len(cnts) > k:
                cnts[s[left]] -= 1
                if cnts[s[left]] == 0:
                    del cnts[s[left]]
                left += 1
                ans = max(ans, right - left + 1)
        return ans
    
S = Solution()
s = "eceba"
k = 2
print(S.find_longest_substring(s, k))