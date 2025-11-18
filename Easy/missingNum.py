from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lookupNums = set(nums)
        nums.sort()
        for i in range(0, len(nums) + 1):
            if i not in lookupNums:
                return i
            
s = Solution()
nums = [3,0,1]
print(s.missingNumber(nums))