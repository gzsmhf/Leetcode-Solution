'''
Runtime: 36 ms, faster than 88.20% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.9 MB, less than 55.46% of Python3 online submissions for Excel Sheet Column Number.
'''

import math

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        l = len(columnTitle)
        res = 0
        for i in range(l):
            res += (ord(columnTitle[i]) - 64) * math.pow(26, i)
        return int(res)

s = Solution()
print(s.titleToNumber("A"))