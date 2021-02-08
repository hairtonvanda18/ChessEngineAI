import pygame as p
import ChessEngine
import ChessAi    
    
WIDTH = HEIGHT = 400
DIMENSION = 5 
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ["bR","bN","bB","bQ","bK",
            "bp","wp","wR","wN","wB","wQ","wK"]
    for piece in pieces:
        IMAGES[piece] =p.transform.scale( p.image.load("Images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))
def highlightSquares(screen,gs,validmoves,sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            s = p.Surface((SQ_SIZE,SQ_SIZE))
            s.set_alpha(100)
            s.fill(p.Color("blue"))
            screen.blit(s,(c*SQ_SIZE,r*SQ_SIZE))
            s.fill(p.Color("yellow"))
            for move in validmoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s,(move.endCol*SQ_SIZE,move.endRow*SQ_SIZE))
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validmoves = gs.getValidMoves()
    moveMade = False
    loadImages()
    running = True
    animate = False
    sqSelected = ()
    playerClicks = []
    gameOver = False
    playerOne = True
    playerTwo = False
    while running:
        humansTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver and humansTurn:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    if sqSelected == (row,col):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row,col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 2:
                        move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                        print(move.getChessNotation())
                        for i in range(len(validmoves)):
                            if move == validmoves[i]:
                                gs.makeMove(validmoves[i])
                                moveMade = True 
                                animate = True
                                sqSelected = ()
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    animate = False
                if e.key == p.K_r:
                    gs = ChessEngine.GameState()
                    validmoves= gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = ()
                    moveMade = False
                    animate = False
        if not gameOver and not humansTurn:
             AIMove = ChessAi.findBestMove(gs,validmoves)
             if AIMove is None:
                 AIMove = ChessAi.findRandomMove(validmoves)
             gs.makeMove(AIMove)
             moveMade = True
             animate = True
        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1],screen,gs.board,clock)
            validmoves = gs.getValidMoves()
            moveMade = False
            animate = False
        drawGameState(screen,gs,validmoves,sqSelected)
        if gs.checkMate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen,"As Pretas ganham por Checkmate")
            else:
                drawText(screen,"As Brancas ganham por Checkmate")
        elif gs.staleMate:
            gameOver = True
            drawText(screen,"Stalemate")
        clock.tick(MAX_FPS)
        p.display.flip()
        

def drawGameState(screen,gs,validmoves,sqSelected):
    drawBoard(screen)
    drawPieces(screen,gs.board)
    highlightSquares(screen,gs,validmoves,sqSelected)

def drawBoard(screen):
    global colors
    colors = [p.Color("gray"),p.Color("white")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
def animateMove(move,screen,board,clock):
    global colors
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 10
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    for frame in range(frameCount+1):
        r,c = ((move.startRow + dR*frame/frameCount,move.startCol + dC*frame/frameCount))
        drawBoard(screen)
        drawPieces(screen,board)
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = p.Rect(move.endCol*SQ_SIZE,move.endRow*SQ_SIZE,SQ_SIZE,SQ_SIZE)
        p.draw.rect(screen,color,endSquare)
        if move.pieceCaptured != "--":
            screen.blit(IMAGES[move.pieceCaptured],endSquare)
        screen.blit(IMAGES[move.pieceMoved],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
        p.display.flip()
        clock.tick(60)

def drawText(screen,text):
    font = p.font.SysFont('Helvitca', 20, True, False)
    textObject = font.render(text,0,p.Color('Black'))
    textLocation= p.Rect(0,0,WIDTH,HEIGHT).move(WIDTH/2- textObject.get_width()/2,HEIGHT/2-textObject.get_height()/2)
    screen.blit(textObject,textLocation)
main()


