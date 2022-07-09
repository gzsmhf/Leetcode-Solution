'''
Runtime: 48 ms, faster than 71.58% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 5.51% of Python3 online submissions for Merge Sorted Array.
'''

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        if n == 0:
            return
        while len(nums1) > m:
            nums1.pop(m)
        while j < n:
            if i == len(nums1):
                nums1.append(nums2[j])
                j += 1
            elif nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
            else:
                while True:
                    i += 1
                    if i == len(nums1):
                        nums1.append(nums2[j])
                        j += 1
                        break
                    if nums2[j] <= nums1[i]:
                        nums1.insert(i, nums2[j])
                        j += 1
                        break
        return

s = Solution()
'''nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3'''
nums1 = []
m = 0
nums2 = [1]
n = 1
s.merge(nums1, m, nums2, n)
print(nums1)