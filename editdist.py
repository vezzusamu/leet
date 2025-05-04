class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = defaultdict(int)

        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i, j)]
            if i == l1:
                return l2 - j
            if j == l2:
                return l1 - i
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i+1, j+1)
                return dp[(i, j)]
            ret = min(dfs(i+1, j), dfs(i, j+1))
            ret = min(ret,dfs(i + 1, j+1))
            dp[(i, j)] = ret + 1
            return ret + 1
        return dfs(0,0)

        
                