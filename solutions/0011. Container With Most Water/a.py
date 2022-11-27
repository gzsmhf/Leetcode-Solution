'''
Runtime: 1084 ms, faster than 6.50% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.5 MB, less than 75.78% of Python3 online submissions for Container With Most Water.
'''

#用双指针分别指向数组的头尾计算面积，逐渐合拢
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            if height[start] >= height[end]:
                a = height[end] * (end - start)
                area = max(a, area)
                end -= 1
            else:
                a = height[start] * (end - start)
                area = max(a, area)
                start += 1
        return area