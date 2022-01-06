'''
Runtime: 67 ms, faster than 44.62% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 14.1 MB, less than 99.51% of Python3 online submissions for Zigzag Conversion.
'''

#找到zigzag的通项公式直接拼接
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ls = len(s)
        if ls <= 2 or numRows == 1:
            return s
        rowSize = (numRows - 1) * 2
        res = ''
        for i in range(numRows):
            for j in range(ls // rowSize + 1):
                a = j * rowSize + i
                if a < ls:
                    res += s[a]
                if i != 0 and i != numRows - 1:
                    a = (j + 1) * rowSize - i
                    if a < ls:
                        res += s[a]
        return res