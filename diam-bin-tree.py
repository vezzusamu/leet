# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        largestDiam = 0
        def dOBTA(root):
            nonlocal largestDiam
            if not root:
                return 0
            l = dOBTA(root.left)
            r = dOBTA(root.right)
            largestDiam = max(largestDiam, l + r)

            return max(l, r) + 1
        dOBTA(root)
        return largestDiam