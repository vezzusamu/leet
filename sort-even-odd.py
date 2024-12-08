# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def moveForeword(self, head: Optional[ListNode]) -> None:
        if head.next:
            if head.val > head.next.val:
                tmp = head.val
                head.val = head.next.val
                head.next.val = tmp
                self.moveForeword(head.next)

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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev

        while second:
            tmp = head.next
            tmp2 = second.next
            head.next = second
            second.next = tmp
            second = tmp2
            head = head.next.next
            
        