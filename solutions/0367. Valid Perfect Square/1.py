"""
执行用时：28 ms, 在所有 Python3 提交中击败了97.35% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了72.45% 的用户
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
            
s = Solution()
print(s.isPerfectSquare(16))