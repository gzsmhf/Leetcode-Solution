'''
Runtime: 32 ms, faster than 61.53% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.2 MB, less than 64.37% of Python3 online submissions for Letter Combinations of a Phone Number.
'''

class Solution:
    
    def letterCombinations(self, digits: str):
        dic = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        res = []
        for char in digits:
            if len(res) == 0:
                res = dic[char]
            else:
                res = [x+y for x in res for y in dic[char]]
        return res