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