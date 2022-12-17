from typing import List
import time

# 执行用时：52 ms, 在所有 Python3 提交中击败了88.05% 的用户
# 内存消耗：16.4 MB, 在所有 Python3 提交中击败了46.19% 的用户

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        max_number = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                i += 1
                continue
            else:
                max_number += 1
                i += 1
                j += 1
        return max_number

s =Solution()
start = time.perf_counter()
print(s.findContentChildren([1,2], [1,2,3]))
print(f"time cost is: {time.perf_counter() - start}s")