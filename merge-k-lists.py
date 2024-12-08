# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dummy pointer
        ret_first = r = ListNode(0)
        if len(lists) == 0:
            return 
        min_p = 0
        while len(lists) > 0:
            for (i, el) in enumerate(lists):
                if el.val <= lists[min_p].val:
                    min_p = i
            r.next = ListNode(lists[min_p].val)
            r = r.next
            lists[min_p] = lists[min_p].next
            if lists[min_p] is None:
                del lists[min_p]
            min_p = 0
        return ret_first.next
