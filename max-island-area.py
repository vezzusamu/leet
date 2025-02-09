class Solution:
    def my_sol_maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0, 1],[-1, 0],[0, -1]]
        ROW, COL = len(grid), len(grid[0])
        max_v = 2
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1:
                    grid[i][j] = max_v
                    max_v += 1
                for x, y in directions:
                    x += i
                    y += j
                    if (x < 0) or (y < 0) or (x >= ROW) or (y >= COL) or (grid[x][y] == 0):
                        continue
                    if grid[x][y] == 1:
                        grid[x][y] = grid[i][j]
                    else:
                        grid[x][y] = min(grid[x][y], grid[i][j])
                        grid[i][j] = grid[x][y]
        counts = {}
        m = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] > 1:
                    r = counts.get(grid[i][j], 0) + 1
                    counts[grid[i][j]] = r
                    m = max(r, m)
        return m
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0, 1],[-1, 0],[0, -1]]
        ROW, COL = len(grid), len(grid[0])
        max_a = 0

        def bfs(r1, c1):
            q = deque()
            grid[r1][c1] = 0
            q.append((r1, c1))
            res = 1
            while(q):
                r, c = q.popleft()
                for x, y in directions:
                    x += r
                    y += c
                    if (x < 0) or (y < 0) or (x >= ROW) or (y >= COL) or (grid[x][y] == 0):
                        continue
                    else:
                        grid[x][y] = 0
                        res += 1
                        q.append((x,y))
            return res
                

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    continue
                max_a = max(max_a, bfs(i, j))
        return max_a
