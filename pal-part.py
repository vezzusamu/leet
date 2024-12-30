class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPal(s) -> bool:
            if not s:
                return True
            if len(s) < 2:
                return True
            if s[0] == s[-1]:
                return isPal(s[1:-1])

        ret = []
        part = []

        def dfs(i):
            if i >= len(s):
                ret.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPal(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
                           
        dfs(0)
        return ret
    