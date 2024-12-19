# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        def goodNodesApp(root, maxVal):
            if root:
                if root.val >= maxVal:
                    return 1 + goodNodesApp(root.left, root.val) + goodNodesApp(root.right, root.val)
                return goodNodesApp(root.left, maxVal) + goodNodesApp(root.right, maxVal)
            return 0
        return goodNodesApp(root, -9999999)
