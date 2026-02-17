from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for temp in range(n):
            while stack and temperatures[stack[-1]] < temperatures[temp]:
                j = stack.pop()
                ans[j] = temp - j 
            stack.append(temp)

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73])) # return [1,1,4,2,1,1,0,0]
    print(sol.dailyTemperatures([40,35,32,37,50]))
    print(sol.dailyTemperatures([43,42,30,35,34,50,51,50]))
    print(sol.dailyTemperatures([5,4,3,2,1,100]))
    print(sol.dailyTemperatures([5,4,3,2,1]))