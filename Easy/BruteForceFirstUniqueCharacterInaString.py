from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashCnt = Counter(s)

        for i, letter in enumerate(s):
            if hashCnt[letter] == 1:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    s = "leetcode"
    print(f"First unique character in '{s}' is at index:", sol.firstUniqChar(s))
    s = "loveleetcode"
    print(f"First unique character in '{s}' is at index:", sol.firstUniqChar(s))
    s = "aabb"
    print(f"First unique character in '{s}' is at index:", sol.firstUniqChar(s)) 
    