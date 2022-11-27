'''
Runtime: 741 ms, faster than 73.40% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 32 MB, less than 13.94% of Python3 online submissions for Contains Duplicate II.
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        kk = {}
        for i in range(len(nums)):
            if nums[i] not in kk.keys():
                kk[nums[i]] = [i]
            else:
                kk[nums[i]].append(i)
        for key, v in kk.items():
            if len(v) > 1:
                for i in range(1, len(v)):
                    if v[i] - v[i-1] <= k:
                        return True
        return False