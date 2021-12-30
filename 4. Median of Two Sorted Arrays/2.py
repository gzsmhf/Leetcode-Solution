'''
Runtime: 126 ms, faster than 14.43% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.4 MB, less than 93.69% of Python3 online submissions for Median of Two Sorted Arrays.
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        nums1.sort()
        ln = len(nums1)
        if ln % 2 != 0:
            return nums1[ln // 2]
        else:
            return (nums1[ln//2-1] + nums1[ln//2]) / 2