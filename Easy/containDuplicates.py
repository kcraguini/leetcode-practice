from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNum = set(nums)

        return len(setNum) != len(nums)
    

sol = Solution()
nums = [1,2,3,1]
print(sol.hasDuplicate(nums))   