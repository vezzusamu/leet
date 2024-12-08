# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def _height(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return (self.isBalanced(root.left) and self.isBalanced(root.right))
        
    def isBalanced_dfs(self, root) -> bool:
        if not root:
            return True
        val = self.isBalanced_app(root)
        if val == -1:
            return False
        return True


    def isBalanced_dfs_app(self, root) -> int:
        if not root:
            return 0

        left = self.isBalanced_app(root.left)
        right = self.isBalanced_app(root.right)

        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1+max(left, right)