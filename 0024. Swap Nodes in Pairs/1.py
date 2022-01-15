'''
Runtime: 32 ms, faster than 66.81% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.2 MB, less than 78.14% of Python3 online submissions for Swap Nodes in Pairs.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = []
        while head:
            l.append(head)
            head = head.next
        for i in range(0, len(l), 2):
            if i+1 < len(l):
                l[i], l[i+1] = l[i+1], l[i]
        for i in range(len(l) - 1):
            l[i].next = l[i+1]
        l[-1].next = None
        return l[0]