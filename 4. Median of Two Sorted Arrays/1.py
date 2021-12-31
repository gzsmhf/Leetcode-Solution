'''
Runtime: 141 ms, faster than 11.09% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.3 MB, less than 99.16% of Python3 online submissions for Median of Two Sorted Arrays.
'''

import bisect

#遍历nums2的值，用python的二分库获取其在nums1中插入的位置，然后插入
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        for n in nums2:
            i = bisect.bisect_left(nums1, n)
            nums1.insert(i, n)
        ln = len(nums1)
        if ln % 2 != 0:
            return nums1[ln // 2]
        else:
            return (nums1[ln//2-1] + nums1[ln//2]) / 2