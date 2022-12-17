from typing import List
import time

# 执行用时：64 ms, 在所有 Python3 提交中击败了90.93% 的用户
# 内存消耗：25.1 MB, 在所有 Python3 提交中击败了12.75% 的用户

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sn = set(range(1, len(nums) + 1))
        return list(sn.difference(set(nums)))

s =Solution()
start = time.perf_counter()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(f"time cost is: {time.perf_counter() - start}s")