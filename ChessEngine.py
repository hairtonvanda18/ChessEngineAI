
class GameState():
    def __init__(self):
        self.board=[
            ["bR","bN","bB","bQ","bK"],
            ["bp","bp","bp","bp","bp"],
            ["--","bp","--","--","--"],
            ["wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK"]
        ]
        self.moveFunctions = {'p':self.getPawnMoves,"R":self.getRookMoves,"N":self.getNightMoves,"K":self.getKingMoves,"Q":self.getQueenMoves,"B":self.getBishopMoves}
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
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r,c,moves)
        return moves
    def getPawnMoves(self,r,c,moves):
        if self.whiteToMove:
            if self.board[r-1][c] == "--":
                moves.append(Move((r,c),(r-1,c),self.board))
            if c-1 >= 0:
                if self.board[r-1][c-1][0] == 'b':
                    moves.append(Move((r,c),(r-1,c-1),self.board))
            if c+1 <= 4:
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(Move((r,c),(r-1,c+1),self.board))
        else:
            if self.board[r+1][c] == "--":
                moves.append(Move((r,c),(r+1,c),self.board))
            if c-1 >= 0:
                if self.board[r+1][c-1][0] == 'w':
                    moves.append(Move((r,c),(r+1,c-1),self.board))
            if c+1 <= 4:
                if self.board[r+1][c+1][0] == 'w':
                    moves.append(Move((r,c),(r+1,c+1),self.board))


    def getRookMoves(self,r,c,moves):
        pass
    def getBishopMoves(self,r,c,moves):
        pass
    def getNightMoves(self,r,c,moves):
        pass
    def getQueenMoves(self,r,c,moves):
        pass
    def getKingMoves(self,r,c,moves):
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
        self.moveId = self.startRow*1000 + self.startCol * 100 + self.endRow*10 + self.endCol
    def __eq__(self,other):
        if isinstance(other,Move):
            return self.moveId == other.moveId
        return False
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol) 
    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]     