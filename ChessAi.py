import random
pieceScore = {"K": 0,"Q": 10,"R": 5, "B": 3, "N" :3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0 
def findRandomMove(validmoves):
    return validmoves[random.randint(0,len(validmoves)-1)]
def findBestMove(gs,validmoves):
    turnMultiplier = 1 if gs.whiteToMove else -1

    oppMinMaxScore = CHECKMATE
    bestPlayerMove = None
    for playerMove in validmoves:
        gs.makeMove(playerMove)
        oppMoves=gs.getValidMoves()
        random.shuffle(oppMoves)
        oppMaxScore = -CHECKMATE
        for oppMove in oppMoves:
            gs.makeMove(oppMove)
            if gs.checkMate:
                score = -turnMultiplier*CHECKMATE
            elif gs.staleMate:
                score = STALEMATE
            score = -turnMultiplier * scoreMaterial(gs.board)
            if score > oppMaxScore:
                oppMaxScore= score
                bestPlayerMove= playerMove
            gs.undoMove()
        if oppMaxScore < oppMinMaxScore:
            oppMinMaxScore = oppMinMaxScore
            bestPlayerMove = playerMove
        gs.undoMove()
    return bestPlayerMove
def scoreMaterial(board):
    score = 0 
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]

    return score