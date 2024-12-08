class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return 0
        
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.depth(root)
        return self.res

    def depth(self, root: Optional[TreeNode]):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.res = max(self.res, l+r)
        return max(l,r) + 1