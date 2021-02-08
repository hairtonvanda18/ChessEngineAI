
class GameState():
    def __init__(self):
        self.board=[
            ["bR","bN","bB","bQ","bK"],
            ["bp","bp","bp","bp","bp"],
            ["--","--","--","--","--"],
            ["wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK"]
        ]
        self.whiteToMove = True
        self.moveLog=[]
    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
    def getValidMoves(self):
        return self.getAllPossibleMoves()
    def getAllPossibleMoves(self):
        pass
class Move():
    ranksToRows = {"1": 4,"2": 3,"3": 2,"4": 1,"5": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a":0,"b":1,"c":2,"d":3,"e":4}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol) 
    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]     