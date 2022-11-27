'''
Runtime: 32 ms, faster than 91.95% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.4 MB, less than 31.70% of Python3 online submissions for Merge Two Sorted Lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 将链表转换成数组，对数组按照val排序，遍历列表修复链表关系
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while list1 is not None or list2 is not None:
            if list1:
                l.append(list1)
                list1 = list1.next
            if list2:
                l.append(list2)
                list2 = list2.next
        l.sort(key=lambda x: x.val)
        for i in range(1, len(l)):
            l[i-1].next = l[i]
        if l:
            l[-1].next = None
            return l[0]
        else:
            return None