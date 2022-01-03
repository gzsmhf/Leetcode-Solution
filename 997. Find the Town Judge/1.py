'''
Runtime: 1121 ms, faster than 8.22% of Python3 online submissions for Find the Town Judge.
Memory Usage: 19.1 MB, less than 23.32% of Python3 online submissions for Find the Town Judge.
'''

#将被信任的人的index和count存入dict中，按照count降序排序再判断第一个元素是否是judge
class Solution:
    def findJudge(self, n: int, trust) -> int:
        if not trust:
            if n == 1:
                return 1
            else:
                return -1
        res = {}
        for t in trust:
            if t[1] not in res:
                res[t[1]] = 1
            else:
                res[t[1]] += 1
        res = sorted(res.items(), key=lambda x: x[1], reverse=True)
        if res[0][1] == n - 1:
            if len(res) > 1 and res[1][1] == n - 1:
                return -1
            elif res[0][0] in [x[0] for x in trust]:
                return -1
            else:
                return res[0][0]
        else:
            return -1