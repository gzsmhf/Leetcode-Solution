'''
Runtime: 98 ms, faster than 80.04% of Python3 online submissions for Power of Three.
Memory Usage: 13.9 MB, less than 58.07% of Python3 online submissions for Power of Three.
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0 and n > 0:
            n //= 3
        return n == 1