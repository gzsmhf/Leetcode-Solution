import bisect

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