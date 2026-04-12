from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lenNum1 = len(nums1)
        lenNum2 = len(nums2)

        ans = [-1] * lenNum1

        for i in range(lenNum1):
            for j in range(lenNum2):

        return ans

if '__name__' == '__main__':
    sol = Solution()
    n1 = [4,1,2]
    n2 = [1,3,4,2]

    print(sol.nextGreaterElement(n1,n2))
