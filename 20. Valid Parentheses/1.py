'''
Runtime: 31 ms, faster than 64.52% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 65.09% of Python3 online submissions for Valid Parentheses.
'''

# 使用堆栈，如果是做边框就压栈，如果是右边框就查看堆栈最端是不是匹配
class Solution:
    def isValid(self, s: str) -> bool:
        ss = []
        for char in s:
            if char in ('(', '[', '{'):
                ss.append(char)
            elif char == ')':
                if len(ss) == 0 or ss[-1] != '(':
                    return False
                else:
                    ss.pop()
            elif char == ']':
                if len(ss) == 0 or ss[-1] != '[':
                    return False
                else:
                    ss.pop()
            elif char == '}':
                if len(ss) == 0 or ss[-1] != '{':
                    return False
                else:
                    ss.pop()
        return len(ss) == 0