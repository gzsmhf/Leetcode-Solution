from typing import List
import time

# 执行用时：124 ms, 在所有 Python3 提交中击败了92.64% 的用户
# 内存消耗：23.3 MB, 在所有 Python3 提交中击败了89.94% 的用户

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_number = prices[0]
        max_number = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_number:
                min_number = prices[i]
                max_number = prices[i]
                continue
            if prices[i] > max_number:
                max_number = prices[i]
                profit = max(profit, max_number - min_number)
        return profit

s =Solution()
start = time.perf_counter()
print(s.maxProfit([7,6,4,3,1]))
print(f"time cost is: {time.perf_counter() - start}s")