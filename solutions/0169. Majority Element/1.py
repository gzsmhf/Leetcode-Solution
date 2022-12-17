from typing import List
import time

# 执行用时：40 ms, 在所有 Python3 提交中击败了84.54% 的用户
# 内存消耗：16.2 MB, 在所有 Python3 提交中击败了96.77% 的用户

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 3:
            return nums[0]
        ss = set(nums)
        for s in ss:
            if nums.count(s) > l/2:
                return s


s =Solution()
start = time.perf_counter()
print(s.majorityElement([2,2,1,1,1,2,2]))
print(f"time cost is: {time.perf_counter() - start}s")