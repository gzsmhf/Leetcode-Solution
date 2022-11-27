"""
执行用时：48 ms, 在所有 Python3 提交中击败了74.50% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了50.82% 的用户
"""

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall("[a-z0-9]", s.lower()))
        return s == s[::-1]
    
so = Solution()
print(so.isPalindrome("A man, a plan, a canal: Panama"))