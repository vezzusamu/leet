class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = {}
        for el in prerequisites:
            r = req.get(el[0], [])
            r.append(el[1])
            req[el[0]] = r

        enc = []
        def dfs(k):
            if k in enc:
                return False
            if not(len(req.get(k, []))):
                return True
            enc.append(k)
            for r in req.get(k, []):
                if not dfs(r):
                    return False
            enc.remove(k)
            req[k] = []
            return True

        for k in range(numCourses):
            if not dfs(k):
                return False
        return True