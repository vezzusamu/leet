class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            column = []
            for j in range(9):
                if contains(row, board[i][j]) or  contains(column, board[j][i]):
                    return False
                if (board[i][j]  != "."):
                    row.append(board[i][j])
                if (board[j][i] != "."):
                    column.append(board[j][i])
            print(column)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] == ".":
                            continue
                        if contains(square, board[i+k][j+l]):
                            return False
                        square.append(board[i+k][j+l])
            
        return True
    
    def isValidSudoku_extra(self, board: List[List[str]]) -> bool:
        data = []
        #flatten the board into an 1-d array.
        for row in board:
            data = data + row
        #use list's slice operation to get rows and columns
        for i in range(9):
            
            temp = data[9*i:9*(i+1)]
			#consider only digits
            temp = [elem for elem in temp if elem!="."]
            #use set to determine the existence of duplicates
            #Here I check the row duplicates
            if len(temp)!=len(set(temp)):
                return False
                
            #Takes elements i, i+9, 2i+9, by using that tecnique I can take the columns
            temp = data[i::9]
            temp = [elem for elem in temp if elem!="."]
            if len(temp)!=len(set(temp)):
                return False

        #get 3x3 subboard
        for i in range(0,9,3):
            for j in range(3):
                temp = data[i*9+j*3:i*9+(j+1)*3] + data[(i+1)*9+j*3:(i+1)*9+(j+1)*3] + data[(i+2)*9+j*3:(i+2)*9+(j+1)*3]
                temp = [elem for elem in temp if elem!="."]
                if len(temp)!=len(set(temp)):
                    return False
                    
        return True
        