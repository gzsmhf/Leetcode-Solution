'''
Runtime: 35 ms, faster than 89.30% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 55.97% of Python3 online submissions for Power of Four.
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        nn = [4**x for x in range(16)]
        return n in nn