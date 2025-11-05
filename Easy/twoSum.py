from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for num in range(len(nums)):
            needPair = target - nums[num]
            if needPair in pairs.keys():
                return [num, pairs[needPair]]
            else: 
                pairs[nums[num]] = num

s = Solution()
nums = [2,7,11,15]
target = 9

print(s.twoSum(nums, target))
