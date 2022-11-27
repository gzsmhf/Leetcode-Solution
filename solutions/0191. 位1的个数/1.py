"""
执行用时：32 ms, 在所有 Python3 提交中击败了91.51% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了60.68% 的用户
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')