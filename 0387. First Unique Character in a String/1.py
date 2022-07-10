'''
Runtime: 130 ms, faster than 73.76% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.1 MB, less than 58.55% of Python3 online submissions for First Unique Character in a String.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        if l == 1:
            return 0
        for i in range(len(s) - 1):
            if s.find(s[i]) == i:
                if s.find(s[i], i+1) == -1:
                    return i
        return -1 if s.find(s[-1]) != l-1 else l-1