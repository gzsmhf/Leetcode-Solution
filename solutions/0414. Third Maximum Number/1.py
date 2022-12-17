from typing import List
import time

# 执行用时：32 ms, 在所有 Python3 提交中击败了92.09% 的用户
# 内存消耗：15.9 MB, 在所有 Python3 提交中击败了53.67% 的用户

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dl = list(set(nums))
        if len(dl) < 3:
            return max(dl)
        else:
            dl.sort()
            return dl[-3]

s =Solution()
start = time.perf_counter()
print(s.thirdMax([2,2,3,1]))
print(f"time cost is: {time.perf_counter() - start}s")