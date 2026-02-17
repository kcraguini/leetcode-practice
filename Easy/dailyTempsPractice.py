from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)

        return ans
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73])) # return [1,1,4,2,1,1,0,0]
    print(sol.dailyTemperatures([40,35,32,37,50]))