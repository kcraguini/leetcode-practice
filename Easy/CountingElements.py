from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        lookupNuns = set(arr)
        cnt = 0

        for i in range(len(arr)):
            if arr[i] + 1 in lookupNuns:
                cnt += 1
        return cnt
    
s = Solution()
arr = [1,2,3]
print(s.countElements(arr))
arr2 = [1,1,3,3,5,5,7,7]
print(s.countElements(arr2))
arr3 = [1,1,2,2]
print(s.countElements(arr3))