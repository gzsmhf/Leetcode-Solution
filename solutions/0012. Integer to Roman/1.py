'''
Runtime: 74 ms, faster than 12.85% of Python3 online submissions for Integer to Roman.
Memory Usage: 14.1 MB, less than 95.43% of Python3 online submissions for Integer to Roman.
'''

class Solution:
    dic = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
    
    def intToRoman(self, num: int) -> str:
        res = ''
        for k, v in self.dic.items():
            res += v * (num // k)
            num %= k
        return res.replace('VIIII', 'IX').replace('IIII', 'IV').replace('LXXXX', 'XC').replace('XXXX', 'XL').replace('DCCCC', 'CM').replace('CCCC', 'CD')