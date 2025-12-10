from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches:List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[loser] += 1
            
        zeroL = []
        oneL = []
        
        for player, loss_cnt in losses.items():
            if loss_cnt == 0:
                zeroL.append(player)
            elif loss_cnt == 1:
                oneL.append(player)
        
        return [sorted(zeroL), sorted(oneL)]
    
    
    
    
    
sol = Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(sol.findWinners(matches))
