'''
Runtime: 60 ms, faster than 86.43% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.8 MB, less than 5.30% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
'''

class Solution:
    def twoSum(self, numbers, target: int):
        start, end = 0, len(numbers) - 1
        while start != end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start+1, end+1]
            if s > target:
                end -= 1
            else:
                start += 1