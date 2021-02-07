
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
class Move():
    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
