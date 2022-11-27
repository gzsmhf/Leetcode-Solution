'''
Runtime: 205 ms, faster than 93.77% of Python3 online submissions for Reverse String.
Memory Usage: 18.4 MB, less than 47.06% of Python3 online submissions for Reverse String.
'''

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while True:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            if i == j or j - i < 0:
                return