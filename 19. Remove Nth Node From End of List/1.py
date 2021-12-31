'''
Runtime: 57 ms, faster than 5.18% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.2 MB, less than 76.89% of Python3 online submissions for Remove Nth Node From End of List.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 把链表转换成字典，key放节点value放index
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = {}
        count = 0
        while head:
            l[count] = head
            head = head.next
            count += 1
        lh = len(l)
        if lh == 1:
            return None
        index = lh - n
        if index - 1 >= 0:
            l[index-1].next = l[index+1] if index+1<lh else None
        else:
            l.pop(0)
        return list(l.values())[0]