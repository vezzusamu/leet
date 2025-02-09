class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[0, 1],[-1, 0],[0, -1]]
        ROW, COL = len(grid), len(grid[0])

        def bfs(r1, c1):
            q = deque()
            q.append((r1, c1))
            while(q):
                r, c = q.popleft()
                for x, y in directions:
                    x += r
                    y += c
                    if (x < 0) or (y < 0) or (x >= ROW) or (y >= COL) or (grid[x][y] == -1) or (grid[x][y] == 0):
                        continue
                    else:
                        if grid[x][y] > grid[r][c] + 1:
                            q.append((x,y))
                        grid[x][y] = min(grid[r][c] + 1, grid[x][y])
                        
                

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    bfs(i, j)