'''
Runtime: 38 ms, faster than 98.97% of Python3 online submissions for Ransom Note.
Memory Usage: 14.2 MB, less than 52.35% of Python3 online submissions for Ransom Note.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #b = list(magazine)
        for s in ransomNote:
            if s in magazine:
                magazine = magazine.replace(s, "", 1)
            else:
                return False
        return True