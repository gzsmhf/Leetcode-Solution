'''
Runtime: 44 ms, faster than 82.73% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.4 MB, less than 27.97% of Python3 online submissions for Roman to Integer.
'''

#对第一种方法的优化，以空间换时间
class Solution:
    dic = {'MMM':3000, 'MM':2000, 'M':1000, 'CM':900, 'D':500, 'CD':400, 'CCC':300, 'CC':200, 'C':100, 'XC':90, 'L':50, 'XL':40, 'XXX':30, 'XX':20, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
    
    def romanToInt(self, s: str) -> int:
        n = 0
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i:i+3] in self.dic.keys():
                n += self.dic[s[i:i+3]]
                i += 3
            elif i+1 < len(s) and s[i:i+2] in self.dic.keys():
                n += self.dic[s[i:i+2]]
                i += 2
            else:
                n += self.dic[s[i]]
                i += 1
        return n

print(Solution().romanToInt("MMMCXXX"))