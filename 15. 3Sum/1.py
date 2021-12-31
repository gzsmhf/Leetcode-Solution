'''
Runtime: 4789 ms, faster than 15.25% of Python3 online submissions for 3Sum.
Memory Usage: 18 MB, less than 24.93% of Python3 online submissions for 3Sum.
'''

#首先对数组按升序排序，从左至右遍历数组，使用双指针指向目标数组的头尾
class Solution:
    
    def threeSum(self, nums):
        res = []
        ln = len(nums)
        if ln < 3:
            return res
        nums.sort()
        for i in range(ln):
            if nums[i] > 0:
                break
            if i - 1 >= 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, ln - 1
            while l < r:
                a = nums[i] + nums[l] + nums[r]
                if a == 0:
                    tmp = sorted([nums[i], nums[l], nums[r]])
                    if tmp not in res:
                        res.append(tmp)
                    r -= 1
                    l += 1
                elif a > 0:
                    r -= 1
                else:
                    l += 1
        return res
    
print(Solution().threeSum([1,2,-2,-1]))