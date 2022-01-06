'''
Runtime: 52 ms, faster than 91.57% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 6.67% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ''
        tmp = ''
        for char in s:
            if char not in tmp:
                tmp += char
            else:
                if len(tmp) > len(res):
                    res = tmp
                tmp = tmp[tmp.index(char)+1:] + char
        if len(tmp) > len(res):
            res = tmp
        return len(res)