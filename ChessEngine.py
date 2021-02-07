
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
        
