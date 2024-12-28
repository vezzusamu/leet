class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if row >= ROWS or col >= COLS or row < 0 or col < 0 or word[i] != board[row][col]:
                return False

            board[row][col] = "."
            ret = dfs(row - 1, col, i+ 1) or dfs(row, col + 1, i + 1) or dfs(row + 1, col, i + 1) or dfs(row, col - 1, i+ 1)
            if not ret:
                board[row][col] = word[i]
            return ret
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c, 0):
                    return True
        return False

                
        