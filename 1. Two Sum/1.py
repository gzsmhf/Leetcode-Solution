'''
Runtime: 60 ms, faster than 76.11% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 80.42% of Python3 online submissions for Two Sum.
'''

#对数组分组
class Solution:
    def twoSum(self, nums, target: int):
        half = target // 2
        if target % 2 == 0 and nums.count(half) == 2:
            findex = nums.index(half)
            sindex = nums[findex+1:].index(half) + findex + 1
            return [findex, sindex]
        a, b = [], []
        for num in nums:
            a.append(num) if num > half else b.append(num)
        if len(a) > len(b):
            a, b = b, a
        for num in a:
            if target - num in b:
                return sorted([nums.index(num), nums.index(target - num)])