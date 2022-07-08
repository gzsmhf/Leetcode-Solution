'''
Runtime: 36 ms, faster than 82.34% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 66.48% of Python3 online submissions for Pascal's Triangle.
'''

class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            res = []
            res.append([1])
            res.append([1,1])
            for i in range(2, numRows):
                tmp = [1] * (i + 1)
                for j in range(1, i):
                    t = res[i - 1]
                    tmp[j] = t[j-1] + t[j]
                res.append(tmp)
            return res

s = Solution()
print(s.generate(5))