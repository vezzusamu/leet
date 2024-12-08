# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        els = 1
        tmp = head
        if not tmp:
            return head
        while tmp.next:
            els += 1
            tmp = tmp.next
        els -= n
        if els == 0:
            return head.next
        tmp = head
        print(els)
        while els > 1 and tmp:
            tmp = tmp.next
            els -= 1
        if tmp.next:
            tmp.next = tmp.next.next

        return head
        