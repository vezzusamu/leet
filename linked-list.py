# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        app = head
        prev = None
        next = None
        while app:
            next = app.next 
            app.next = prev
            prev = app
            app = next
        return prev
    
    def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head
        if not head:
            return None

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
            
        
        