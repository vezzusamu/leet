from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        already_v = {}
        if not node:
            return 
        def clone_app(node):
            nonlocal already_v
            if not node:
                return 
            if node.val in already_v:
                return already_v[node.val]
            nodes = []
            curr = Node(node.val, nodes)
            already_v[curr.val] = curr
            for n in node.neighbors:
                clone_app(n)
                nodes.append(already_v[n.val])
            curr.nodes = nodes
            already_v[node.val] = curr
            
        clone_app(node)
        return already_v[node.val]