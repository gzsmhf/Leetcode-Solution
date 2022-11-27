'''
Runtime: 41 ms, faster than 63.73% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 13.8 MB, less than 64.55% of Python3 online submissions for Guess Number Higher or Lower.
'''

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 0
        e = n
        mid = (s + e) // 2
        while True:
            r = guess(mid)
            if r == 0:
                return mid
            if r < 0:
                if mid - s == 1:
                    mid = s
                else:
                    e = mid
                    mid = (s + e) // 2
            else:
                if e - mid == 1:
                    mid = e
                else:
                    s = mid
                    mid = (s + e) // 2