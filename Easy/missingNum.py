from collections import Counter 
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        neededLen = len(nums) + 1
        seenNums = Counter(nums)
        
        for i in range(neededLen):
            if i not in seenNums:
                return i
            
s = Solution()
nums = [3,0,1]
print(s.missingNumber(nums))