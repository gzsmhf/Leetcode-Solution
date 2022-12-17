from typing import List
import time

# 执行用时：36 ms, 在所有 Python3 提交中击败了99.32% 的用户
# 内存消耗：15.8 MB, 在所有 Python3 提交中击败了46.45% 的用户

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if count != i:
                    nums[count], nums[i] = nums[i],nums[count]
                count += 1
                    

s =Solution()
nums = [1]
start = time.perf_counter()
s.moveZeroes(nums)
print(nums)
print(f"time cost is: {time.perf_counter() - start}s")