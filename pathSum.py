# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def path(root, curr, currSum):
            nonlocal paths
            if root == None:
                return 
            curr.append(root.val)
            currSum += root.val
            if root.left == None and root.right == None:
                if currSum == targetSum and len(curr):
                    paths.append(curr)
                return
            path(root.left, copy.copy(curr), currSum )
            path(root.right, copy.copy(curr), currSum )

        path(root,  [], 0)
        return paths