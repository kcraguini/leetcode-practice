from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        distinct = defaultdict(int)

        for arr in arrs:
            for num in arr:
                distinct[num] += 1

        n = len(arrs)
        ans = []
        for i in distinct:
            if distinct[i] == n:
                ans.append(i)

        return sorted(ans)


sol = Solution()
arrs = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(sol.intersection(arrs))  