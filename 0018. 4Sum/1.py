'''
Runtime: 760 ms, faster than 70.77% of Python3 online submissions for 4Sum.
Memory Usage: 14.5 MB, less than 29.26% of Python3 online submissions for 4Sum.
'''

# 复用第15题三相求和代码进行降维处理
class Solution:
    def threeSum(self, nums, target):
        res = []
        ln = len(nums)
        if ln < 3:
            return res
        nums.sort()
        for i in range(ln):
            if nums[i] > 0 and nums[i] > target:
                break
            if i - 1 >= 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, ln - 1
            while l < r:
                a = nums[i] + nums[l] + nums[r]
                if a == target:
                    tmp = sorted([nums[i], nums[l], nums[r]])
                    if tmp not in res:
                        res.append(tmp)
                    r -= 1
                    l += 1
                elif a > target:
                    r -= 1
                else:
                    l += 1
        return res
    
    def fourSum(self, nums, target: int):
        ln = len(nums)
        res = []
        if ln < 4:
            return []
        nums.sort()
        for i in range(ln-3):
            if nums[i] > 0 and nums[i] > target:
                break
            if i - 1 >= 0 and nums[i-1] == nums[i]:
                continue
            tmp = self.threeSum(nums[i+1:], target - nums[i])
            if tmp:
                res.extend([x + [nums[i]] for x in tmp])
        return res