'''
Runtime: 64 ms, faster than 72.03% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14 MB, less than 85.55% of Python3 online submissions for Intersection of Two Arrays II.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            a, b = nums2, nums1
        else:
            a, b = nums1, nums2
        r = []
        for i in a:
            if i in b:
                b.remove(i)
                r.append(i)
        return r