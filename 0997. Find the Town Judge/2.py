'''
Runtime: 1082 ms, faster than 9.31% of Python3 online submissions for Find the Town Judge.
Memory Usage: 18.8 MB, less than 87.18% of Python3 online submissions for Find the Town Judge.
'''

#创建ab两个list，分别放入第i个人信任别人的次数和被别人信任的次数
class Solution:
    def findJudge(self, n: int, trust) -> int:
        a = [0]*n
        b = [0]*n
        for t in trust:
            a[t[0]-1] += 1
            b[t[1]-1] += 1
        for i in range(n):
            if b[i] == n - 1 and a[i] == 0:
                return i+1
        return -1