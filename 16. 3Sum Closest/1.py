'''
Runtime: 92 ms, faster than 97.70% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.2 MB, less than 71.05% of Python3 online submissions for 3Sum Closest.
'''

#模仿15题思路
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        ln = len(nums)
        nums.sort()
        res = 40000
        diff = 20000
        for i in range(ln):
            if nums[i] > 0 and nums[i] > target and nums[i] > res:
                break
            if i - 1 >= 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, ln - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                a = target - s
                if a == 0:
                    return target
                elif abs(a) < diff:
                    diff = abs(a)
                    res = s
                if a < 0:
                    r -= 1
                else:
                    l += 1
        return res