from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0
        
        diff_index = {}
        
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            if one - zero not in diff_index:
                diff_index[one - zero] = i
                
            if one == zero:
                res = one + zero
            else:
                idx = diff_index[one - zero]
                res = max(res, i - idx)
                
        return res
        
sol = Solution()
nums = [1,1,1,0,0,0,0]

print(sol.findMaxLength(nums))