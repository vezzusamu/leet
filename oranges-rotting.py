class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0, 1],[-1, 0],[0, -1]]
        ROW, COL = len(grid), len(grid[0])
        elapsed = 0
        q = deque()
        def bfs(q):
            nonlocal elapsed
            while(q):
                r, c = q.popleft()
                for x, y in directions:
                    x += r
                    y += c
                    if (x < 0) or (y < 0) or (x >= ROW) or (y >= COL) or (grid[x][y] == 0) or (grid[x][y] >= 2):
                        continue
                    else:
                        q.append((x,y))
                        elapsed = max(elapsed, grid[r][c] + 1)
                        grid[x][y] = (grid[r][c] + 1)
                        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i, j))
        bfs(q)
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1
        return max(elapsed - 2,0)