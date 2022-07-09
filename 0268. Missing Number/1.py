'''
Runtime: 133 ms, faster than 97.07% of Python3 online submissions for Missing Number.
Memory Usage: 16.2 MB, less than 6.12% of Python3 online submissions for Missing Number.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nn = set(range(len(nums) + 1)).difference(set(nums))
        for n in nn:
            return n