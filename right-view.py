# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = {}
        
        def bfs(root, level, r_l):
            if not root:
                return
            r = levels.get(level , ( None, -999))
            if r_l >= r[1]:
                levels[level] = (root.val, r_l)
                print(levels)
            bfs(root.left, level + 1, r_l - 1)
            bfs(root.right, level + 1, r_l + 1) 

        bfs(root, 0, 0)
        ret_list = [l[0] for l in levels.values()]
        return ret_list