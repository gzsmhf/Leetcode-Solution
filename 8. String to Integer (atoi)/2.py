'''
Runtime: 40 ms, faster than 27.31% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.1 MB, less than 82.06% of Python3 online submissions for String to Integer (atoi).
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        signal = []
        for char in s.strip():
            if char in ('+', '-'):
                if len(res) != 0:
                    break
                if len(signal) != 0:
                    return 0
                signal.append(char)
            elif char.isdigit():
                res.append(char)
            else:
                break
        l = len(res)
        if l == 0:
            return 0
        n = 0
        for i in range(l):
            n += int(res[i]) * (10 ** (l - i - 1))
        n = -n if signal and signal[0] == '-' else n
        n = -2**31 if n < -2**31 else (2**31-1 if n > 2**31-1 else n)
        return n