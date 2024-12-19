# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val

        def app(root) :
            nonlocal count, res

            if not root:
                return
            app(root.left)
            count -= 1
            if count == 0:
                res = root.val
            app(root.right)
            
        app(root)
        return res