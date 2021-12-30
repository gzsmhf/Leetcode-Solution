'''
Runtime: 48 ms, faster than 95.59% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 92.52% of Python3 online submissions for Palindrome Number.
'''


import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        s = str(x)
        for i in range(math.ceil(len(s) / 2)):
            j = len(s) - i - 1
            if s[i] != s[j]:
                return False
        return True