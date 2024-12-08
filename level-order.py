# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def my_sol_levelOrderN(self, root, n) -> dict:
        ret = {}
        if root is None:
            return ret
        ret[n] = [root.val]
        l = self.levelOrderN(root.left, n+1)
        r = self.levelOrderN(root.right, n+1)
        for i in l.keys():
            ret[i] = ret.get(i, [])
            ret[i].extend(l[i])
            if i in r:
                ret[i].extend(r[i])
        for i in [k for k in r.keys() if k not in l.keys()]:
            ret[i] = ret.get(i, [])
            ret[i].extend(r[i])
        return ret

    def my_sol_levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        ret = self.levelOrderN(root, 0)
        return list(ret.values())
    
    def levelOrder(self, root) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        ret = []
        while q:
            qLen = len(q)
            l = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                ret.append(l)
        return ret
    
    def levelOrder_dfs(self, root) -> List[List[int]]:
        ret_vals = {}

        def dfs(root, depth):
            if not root:
                return
            ret_vals[depth] = ret_vals.get(depth, [])
            ret_vals[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            
        dfs(root, 0)
        return list(ret_vals.values())