'''
Runtime: 94 ms, faster than 30.97% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14.4 MB, less than 59.73% of Python3 online submissions for Regular Expression Matching.
'''

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match('^'+p+'$', s) is not None