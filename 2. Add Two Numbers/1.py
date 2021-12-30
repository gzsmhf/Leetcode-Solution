# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        j = 0
        while l1 is not None or l2 is not None:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            s = n1 + n2 + j
            j = s // 10
            l = ListNode(s % 10, None)
            if len(res) != 0:
                res[-1].next = l
            res.append(l)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if j != 0:
            l = ListNode(j, None)
            res[-1].next = l
        return res[0]