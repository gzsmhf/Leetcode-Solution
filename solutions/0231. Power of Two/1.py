'''
Runtime: 37 ms, faster than 84.91% of Python3 online submissions for Power of Two.
Memory Usage: 13.8 MB, less than 95.28% of Python3 online submissions for Power of Two.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        nn = [2**x for x in range(31)]
        return n in nn