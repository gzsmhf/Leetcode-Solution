from typing import List
import time

# 执行用时：60 ms, 在所有 Python3 提交中击败了75.60% 的用户
# 内存消耗：16 MB, 在所有 Python3 提交中击败了5.03% 的用户

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str, nums)).split("0")))

s =Solution()
start = time.perf_counter()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(f"time cost is: {time.perf_counter() - start}s")