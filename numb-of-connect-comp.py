class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = {}
        for f, t in edges:
            c1 = connections.get(f, set())
            c1.add(t)
            connections[f] = c1
            c2 = connections.get(t, set())
            c2.add(f)
            connections[t] = c2
        r = 0
        visited = set()
        def dfs(el):
            if el in visited:
                return False
            visited.add(el)
            for c in connections.get(el, set()):
                dfs(c)
            return True
        for i in range(n):
            if dfs(i):
                r += 1
        return r