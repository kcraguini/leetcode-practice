from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnts = defaultdict(int)
        cnts[0] = 1 # Needed to account for subarrays that need 0
        ans = cnt = 0

        for num in nums:
            curr += num 
            ans += cnts[curr - k]
            cnts[curr] += 1

        return ans