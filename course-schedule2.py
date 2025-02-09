class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        steps = []
        cycle, visited = set(), set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for c in prereq.get(course, []):                
                res = dfs(c)
                if not res:
                    return False
            
            cycle.remove(course)
            visited.add(course)
            steps.append(course)
            return True
        
        for p in prerequisites:
            l = prereq.get(p[0], [])
            l.append(p[1])
            prereq[p[0]] = l

        for course in range(numCourses):
            if not dfs(course):
                return []
        return steps