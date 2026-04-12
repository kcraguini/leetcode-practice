from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        for idx, num in enumerate(nums):
            while queue and nums[queue[-1]] > nums[num]:
                queue.popleft()

            queue.append(idx) 
            ans.append(nums[queue[0]])
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums =  [1,3,-1,-3,-2,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))