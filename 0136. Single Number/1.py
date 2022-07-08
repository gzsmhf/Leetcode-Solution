'''
Runtime: 123 ms, faster than 99.73% of Python3 online submissions for Single Number.
Memory Usage: 16.8 MB, less than 50.34% of Python3 online submissions for Single Number.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res