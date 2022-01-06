'''
Runtime: 960 ms, faster than 13.91% of Python3 online submissions for Find the Town Judge.
Memory Usage: 19 MB, less than 23.32% of Python3 online submissions for Find the Town Judge.
'''

#在2.py的基础上，把ab两个列表合并成一个。被信任就+1，信任别人就-1，judge的值应该是n-1
class Solution:
    def findJudge(self, n: int, trust) -> int:
        p = [0]*n
        for t in trust:
            p[t[0]-1] -= 1
            p[t[1]-1] += 1
        for i in range(n):
            if p[i] == n - 1:
                return i+1
        return -1