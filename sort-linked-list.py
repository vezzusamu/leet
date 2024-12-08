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


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        app = head
        while app:
            self.moveForeword(app)
            app = app.next
        