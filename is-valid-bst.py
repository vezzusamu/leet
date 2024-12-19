# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTApp(root, l, r) -> bool:
            if not root:
                return True
            if root.val >= r or root.val <= l:
                return False
            return isValidBSTApp(root.left, l, root.val) and isValidBSTApp(root.right, root.val, r)
        return isValidBSTApp(root, -9999999999, 9999999999)