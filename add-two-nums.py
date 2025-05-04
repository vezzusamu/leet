# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2:
            l1.val = l1.val + l2.val
            if l1.val >= 10:
                l1.val = l1.val % 10
                if not l1.next:
                    l1.next = ListNode(1)
                else:
                    l1.next.val += 1
            l1.next = self.addTwoNumbers(l1.next, l2.next)
            return l1
        if l1:
            if l1.val >= 10:
                l1.val = l1.val % 10
                if not l1.next:
                    l1.next = ListNode(1)
                else:
                    l1.next.val += 1
                l1.next = self.addTwoNumbers(l1.next, None)
            return l1
        if l2:
            if l2.val >= 10:
                l2.val = l1.val % 10
                if not l2.next:
                    l2.next = ListNode(1)
                else:
                    l2.next.val += 1
                l2.next = self.addTwoNumbers(None, l2.next)
            return l2

class Solution:
    def addTwoNumbers2Attempt(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addTwoNumbersApp(l1, l2, rep):
            l = ListNode(0)
            if rep:
                l.val += 1
            a = 0
            if l1 and l2:
                l.val += l1.val + l2.val
                if l.val > 9:
                    a = 1
                    l.val -= 10
                l.next = addTwoNumbersApp(l1.next, l2.next, a)
            elif l1:
                l.val += l1.val
                if l.val > 9:
                    a = 1
                    l.val -= 10
                l.next = addTwoNumbersApp(l1.next, l2, a)
            elif l2:
                l.val += l2.val
                if l.val > 9:
                    a = 1
                    l.val -= 10
                l.next = addTwoNumbersApp(l1, l2.next, a)
            if rep or l1 or l2:
                return l
        return addTwoNumbersApp(l1, l2, 0)
