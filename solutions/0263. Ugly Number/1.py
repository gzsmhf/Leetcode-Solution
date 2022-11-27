'''
Runtime: 28 ms, faster than 97.93% of Python3 online submissions for Ugly Number.
Memory Usage: 13.8 MB, less than 58.35% of Python3 online submissions for Ugly Number.
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        if 0 < n < 7:
            return True
        if n <= 0:
            return False
        if n % 2 == 0:
            return self.isUgly(n // 2)
        if n % 3 == 0:
            return self.isUgly(n // 3)
        if n % 5 == 0:
            return self.isUgly(n // 5)
        return False