'''
Runtime: 27 ms, faster than 98.92% of Python3 online submissions for Add Digits.
Memory Usage: 13.8 MB, less than 54.71% of Python3 online submissions for Add Digits.
'''

class Solution:
    def addDigits(self, num: int) -> int:
        n = 0
        for s in str(num):
            n += int(s)
        return n if n < 10 else self.addDigits(n)