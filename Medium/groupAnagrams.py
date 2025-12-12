from typing import List
from collections import defaultdict

class Solution:
    def groupAnagram(self, strs:List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())


sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagram(strs))
