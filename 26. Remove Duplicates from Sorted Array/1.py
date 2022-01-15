'''
Runtime: 178 ms, faster than 14.36% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 6.94% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''

class Solution:
    def removeDuplicates(self, nums) -> int:
        '''
        遍历nums，如果后一个数等于前一个数就抛弃后一个数。
        '''
        i = 0
        while i < len(nums):
            if i != 0:
                if nums[i] == nums[i-1]:
                    nums.pop(i)
                    continue
            i += 1
        return len(nums)