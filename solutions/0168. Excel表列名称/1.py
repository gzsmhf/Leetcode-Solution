"""
执行用时：32 ms, 在所有 Python3 提交中击败了88.57% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了56.99% 的用户
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alist = ['Z'] + [chr(l) for l in range(65, 90)]
        flist = []
        while True:
            if columnNumber < 26:
                flist.append(alist[columnNumber])
                break
            b = columnNumber % 26
            columnNumber = columnNumber // 26
            flist.append(alist[b])
            if b == 0:
                if columnNumber == 1:
                    break
                else:
                    columnNumber -= 1
        return ''.join(flist[::-1])

s = Solution()
print(s.convertToTitle(2147483647))