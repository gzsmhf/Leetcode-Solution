'''
Runtime: 36 ms, faster than 55.96% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.4 MB, less than 55.90% of Python3 online submissions for Longest Common Prefix.
'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[1]
        s = strs.pop(0)
        com = ''
        for i in range(len(s)):
            found = True
            for ss in strs:
                if i > len(ss) - 1 or ss[i] != s[i]:
                    found = False
                    break
            if found:
                com += s[i]
            else:
                break
        return com

print(Solution().longestCommonPrefix(["cir","car"]))