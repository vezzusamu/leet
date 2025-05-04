class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def checkClick(pos) -> str:
            i1, i2 = pos[0], pos[1]
            return board[i1][i2]

        def changeVal(pos, val):
            i1, i2 = pos[0], pos[1]
            board[i1][i2] = val
        
        def getAllDirections(i1,i2):
            ret = []
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    ni1 = i1 + i
                    ni2 = i2 + j
                    if ni1 < 0 or ni2 < 0 or ni1 >= len(board) or ni2 >= len(board[0]):
                        continue
                    ret += [(ni1,ni2)]
            return ret
            
        def propagate(i1,i2):
            if not checkClick((i1,i2)) == "E":
                return
            countMines = 0
            for direction in getAllDirections(i1, i2):
                if checkClick(direction) == "M":
                    countMines += 1
            if countMines == 0:
                changeVal((i1,i2), "B")
                for direction in getAllDirections(i1, i2):
                    propagate(direction[0], direction[1])
            else:
                changeVal((i1,i2), str(countMines))

        if checkClick(click) == "M":
            changeVal(click, "X")
        elif checkClick(click) == "E" :
            propagate(click[0],click[1])
        return board