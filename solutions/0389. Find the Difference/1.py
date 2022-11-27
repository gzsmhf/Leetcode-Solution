'''
Runtime: 39 ms, faster than 86.04% of Python3 online submissions for Find the Difference.
Memory Usage: 14 MB, less than 32.30% of Python3 online submissions for Find the Difference.
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        for i in s:
            t = t.replace(i, "", 1)
        return t[0]