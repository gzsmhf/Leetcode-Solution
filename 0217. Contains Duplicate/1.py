'''
Runtime: 492 ms, faster than 84.90% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.9 MB, less than 72.34% of Python3 online submissions for Contains Duplicate.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))