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