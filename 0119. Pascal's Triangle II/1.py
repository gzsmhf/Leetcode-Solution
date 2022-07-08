'''
Runtime: 27 ms, faster than 98.00% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.9 MB, less than 61.20% of Python3 online submissions for Pascal's Triangle II.
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            now = [1,1]
            for i in range(2, rowIndex + 1):
                nxt = [1] * (i + 1)
                for j in range(1, i):
                    nxt[j] = now[j-1] + now[j]
                now = nxt
            return now