'''
Runtime: 45 ms, faster than 70.44% of Python3 online submissions for Happy Number.
Memory Usage: 13.8 MB, less than 96.80% of Python3 online submissions for Happy Number.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        if n in (1, 7):
            return True
        if n < 10:
            return False
        t = 0
        for nn in str(n):
            t += int(nn) * int(nn)
        if t == 1:
            return True
        else:
            return self.isHappy(t)