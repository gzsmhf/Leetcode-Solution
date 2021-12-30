'''
Runtime: 30 ms, faster than 71.44% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.3 MB, less than 45.74% of Python3 online submissions for Reverse Integer.
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
             return 0
        isNegative = False if x > 0 else True
        if isNegative:
            x = -x
        x = -1 * int(str(x)[::-1]) if isNegative else int(str(x)[::-1])
        x = x if -2**31<=x<=2**31-1 else 0
        return x