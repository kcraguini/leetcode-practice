from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        queue = deque()

        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)


            #removes the elements outside of k
            if queue[0] + k == i:
                queue.popleft()

            # if we want to add the number in the front of the queue but only do so if we pass k elements
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans
    
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums,k))

