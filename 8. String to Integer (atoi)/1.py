'''
Runtime: 41 ms, faster than 17.45% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.1 MB, less than 94.52% of Python3 online submissions for String to Integer (atoi).
'''

import re

class Solution:
    def myAtoi(self, s: str) -> int:
        r = re.search(r'^(\s*)-?\+?[0-9]+', s)
        if r:
            a = r.group(0)
            if a.find('-') != -1 and a.find('+') != -1:
                a = 0
            else:
                a = int(a.replace('+', ''))
        else:
            a = 0
        nmin, nmax = -2**31, 2**31-1
        a = nmin if a < nmin else (nmax if a > nmax else a)
        return a