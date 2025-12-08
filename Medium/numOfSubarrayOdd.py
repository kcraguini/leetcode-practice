from typing import List
from collections import defaultdict 

class Solution:
    def numOfSubarrayOdd(self, nums: List[int], k:int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = 0
        ans = 0
        
        for num in nums:
            curr += num % 2
            ans += prefix[curr - k]
            prefix[curr] += 1
            
        return ans
        
sol = Solution()
nums = [1,1,2,1,1]
k = 3
print(sol.numOfSubarrayOdd(nums, k))