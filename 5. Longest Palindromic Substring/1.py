'''
Runtime: 2904 ms, faster than 32.40% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 81.68% of Python3 online submissions for Longest Palindromic
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ''
        s = '#' + '#'.join(list(s)) + '#'
        for i in range(1, len(s)-1):
            for j in range(1, min(i+1, len(s)-i)):
                if s[i-j] == s[i+j]:
                    if 2*j+1 > len(res):
                        res = s[i-j:i+j+1]
                else:
                    break
        return res.replace('#', '')