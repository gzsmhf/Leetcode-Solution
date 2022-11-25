"""
执行用时：36 ms, 在所有 Python3 提交中击败了80.22% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了50.25% 的用户
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = '0'*(32-len(s)) + s
        return int(s[::-1], 2)