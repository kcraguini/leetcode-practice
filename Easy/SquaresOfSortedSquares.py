"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        result = [0] * numsLen #This creates a list with 0 with the same length of nums
        left =  0
        right = pos = numsLen - 1
        while left <= right:
            #If absolute left is greater than absolute right
            if (abs(nums[left]) > abs(nums[right])):
                result[pos] = nums[left] * nums[left]
                left += 1
            #right is greater or they are the same number
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
             
        return result
    

s = Solution()
nums = [-4,-1,0,3,10]
print(s.sortedSquares(nums))