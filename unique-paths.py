class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n_paths = {}
        for j in range(n):
            n_paths[j] = {}
            n_paths[j][0] = 1
        for i in range(m):
            n_paths[0][i] = 1
        for i in range(1, n):
            for j in range(1, m):
                n_paths[i][j] = n_paths[i - 1][j] + n_paths[i][j - 1]
        return n_paths[n - 1][m - 1]