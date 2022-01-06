'''
Runtime: 150 ms, faster than 30.32% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.6 MB, less than 92.75% of Python3 online submissions for Merge k Sorted Lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 把链表都装进list中，对list排序，然后根据list的顺序修复链表
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for a in lists:
            while a != None:
                l.append(a)
                a = a.next
        l.sort(key=lambda x:x.val)
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        if l:
            l[-1].next = None
            return l[0]
        else:
            return ListNode('')