'''
Runtime: 67 ms, faster than 36.04% of Python3 online submissions for Smallest Integer Divisible by K.
Memory Usage: 14.3 MB, less than 65.77% of Python3 online submissions for Smallest Integer Divisible by K.
'''

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        r = 0
        for i in range(1, k+1):
            r = (r*10+1) % k
            if r == 0:
                return i
        return -1