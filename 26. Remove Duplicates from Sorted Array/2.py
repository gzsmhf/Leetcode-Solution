'''
Runtime: 80 ms, faster than 94.01% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 79.86% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''

class Solution:
    def removeDuplicates(self, nums) -> int:
        '''
        采用双指针方式将不相同的数重新写入nums。
        '''
        basePoint = 0
        enumPoint = 1
        while enumPoint < len(nums):
            if nums[basePoint] != nums[enumPoint]:
                basePoint += 1
                nums[basePoint] = nums[enumPoint]
            enumPoint += 1
        return basePoint + 1