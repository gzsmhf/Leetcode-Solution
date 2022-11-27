'''
Runtime: 36 ms, faster than 99.86% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.2 MB, less than 25.37% of Python3 online submissions for Intersection of Two Arrays.
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            a, b = set(nums2), set(nums1)
        else:
            a, b = set(nums1), set(nums2)
        return list(a.intersection(b))