from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        largeNum = -1
        for count in counts:
            if counts[count] == 1:
                largeNum = max(largeNum, count)
        return largeNum
    
sol = Solution()
nums = [5,7,3,9,4,9,8,3,1]
print(sol.largestUniqueNumber(nums))
