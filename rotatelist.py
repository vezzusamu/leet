# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        newHead = head
        oldHead = head
        
        def appRotate(head, k1):

            nonlocal newHead
            if k1 == -1:
                newHead = head
            if not head:
                return
            print(head.val)
            if not head.next:
                return
            appRotate(head.next, k1 - 1)
        appRotate(head, k)
        head.next = oldHead
        return newHead
    
# Example usage:
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
solution = Solution()
result = solution.rotateRight(head, k)
# Print the rotated list
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")