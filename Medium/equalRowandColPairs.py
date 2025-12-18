from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(arr):
            return tuple(arr)
            
        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1
            
            
        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            curr_col = []
            for row in range(len(grid)):
                curr_col.append(grid[row][col])
            dic2[convert_to_key(curr_col)] += 1
            
        ans = 0 
        for arr in dic:
            ans += dic[arr] * dic2[arr]
    
        return ans
        
sol = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(f"Answer: {sol.equalPairs(grid)}")