# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        l = 0
        def getTail(h):
            nonlocal l
            l+=1
            if not h:
                return h
            if not h.next:
                return h
            return getTail(h.next)
        
        tail = getTail(head)
        
        def appRotate(h1, prev):
            nonlocal oldHeadVal

            if not h1:
                return

            if not h1.next:
                h1.val = prev
                return
            appRotate(h1.next, h1.val)
            if not prev == None:
                h1.val = prev

        k %= l
        for i in range(0, k):
            oldHeadVal = head.val
            appRotate(head, tail.val)
        return head