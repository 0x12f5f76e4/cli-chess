import random, sys

class Piece:
    def __init__(self, name:str, unicode: str, color: int, value: int, fenName: str):
        self.name = name
        self.unicode = unicode
        self.color = color
        self.value = value
        self.fenName = fenName

    def getUnicode(self):
        """Return the unicode's piece."""
        return self.unicode

    def getFen(self):
        """Return the single letter of the piece for the FEN parsing algorithm."""
        return self.fenName
    
    def getValue(self):
        """Return the piece's value."""
        return self.value
    
    def appendPieces(self, p: list):
        """Append the piece to a list, since __main__.Piece object don't have append as an attribute."""
        p.append(self)

    def getName(self):
        return self.name
    
    
def getBoard():
    """Returns a 8x8 board."""
    return [[0 for x in range(8)] for y in range(8)]

def printBoard(board):
    """Prints the lines of the board with the ranks and lines."""
    c = '|'
    line = ''
    for lines in range(len(board)):
        for unicode in range(len(board[lines])):
            if board[lines][unicode] == 0:
                line += c + "  "
            else:
                line += c + board[lines][unicode] + " "
        print(str(8- lines) + " " + line + c)
        line = ''
    print("   A  B  C  D  E  F  G  H")

def setBoard(board: list, fenstr: str, pieces: list):
    #put the pieces inside a dictionnary for O(1) lookup 
    csL = {}
    for piece in pieces:
        csL[piece.getFen()] = piece.getUnicode()
    
    fenstr = fenstr.split('/')
    for x in range(len(fenstr)):
        for j in range(len(fenstr[x])):
            try:
                a = int(fenstr[x][j])
                for i in range(a):
                    board[x][i] = 0
                    
            except ValueError:
                board[x][j] = csL[fenstr[x][j]]
                
def getFenstring(board: list, piece: list):
    fstr = ''
    csL = {}
    for piece in pieces:
        csL[piece.getUnicode()] = piece.getFen()
        
    #loop over the board, check if board[index][index] is == 0, if yes check if last fstr char is an integer, then increment it
    #else get the corresponding value of the board[index][index] from the dictonnary and append it to the fstr
    #add += "/" for each index == 8
    
    return fstr
            
 
def possibleMoves(pieces: list, board: list):
    white = {}
    black = {}
    csL = {}
    for piece in pieces:
        csL[piece.getUnicode()] = piece.getFen()
        if piece.getFen().islower():
            white[piece.getUnicode()] = piece.getFen()
        else:
            black[piece.getUnicode()] = piece.getFen()
    #loop over the board to check each piece's alignments, by incrementing or decrementing their board[x+-1/8][j+-1/8] values
    possibleMoves = {}
    for x in range(len(board)):
        for j in range(len(board[x])):
            if board[x][j] != 0:
                #pawns
                if x >= 1:
                    if csL[board[x][j]] == "p": # check for white pawn, which can only advance in x-1 and x-2 and j-+1 if capture possible
                        # pawn advance of 1 and 2
                        if x <= len(board)-2: # x <= len(board)- 2 so the pawn doesn't go further the promotion line 
                            possibleMoves[csL[board[x][j]], (x,j)] = [(x+2, j), (x+1, j)]
                        #pawn capture for j-1 and j+1
                        if 1<= j<= 6:
                            if board[x+1][j+1] != 0 and '♚' and board[x+1][j+1] not in white: 
                                possibleMoves[csL[board[x][j]], (x, j)] += (x+1, j+1)
                            
                            if board[x+1][j-1] !=0 and '♚' and board[x+1][j-1] not in white:
                                possibleMoves[csL[board[x][j]], (x, j)] += (x+1, j-1)

                        elif j == 0:
                            if board[x+1][j+1]!= 0 and '♚' and board[x+1][j-1] not in white:
                                possibleMoves[csL[board[x][j]], (x, j)] += (x+1, j+1)
                        
                        else:
                            if board[x+1][j-1]!= 0 and '♚' and board[x+1][j-1] not in white:
                                possibleMoves[csL[board[x][j]], (x, j)] += (x+1, j-1)
                
                if csL[board[x][j]] == "P":
                    if len(board) - x >= 1:
                        possibleMoves[csL[board[x][j]], (x,j)] = [(x-2, j), (x-1, j)]
                    
                    if 1 <= j <= 6:
                        if board[x-1][j+1] != 0 and '♔' and board[x-1][j+1] not in black:
                            possibleMoves[csL[board[x][j]], (x, j)] += (x-1, j+1)

                        if board[x-1][j-1] != 0 and '♔' and board[x-1][j-1] not in black:
                            possibleMoves[csL[board[x][j]], (x, j)] += (x-1, j-1)

                    elif j == 0:
                        if board[x-1][j+1] !=0 and '♔' and board[x-1][j+1] not in black:
                            possibleMoves[csL[board[x][j]], (x, j)] += (x-1, j+1)
                    
                    else:
                        if board[x-1][j-1] !=0 and '♔' and board[x-1][j-1] not in black:
                            possibleMoves[csL[board[x][j]], (x, j)] += (x-1, j-1)
                #knights
                if csL[board[x][j]] == "n":
                    #board[x+-2/-1][j+1-1]
                    try:
                        if board[x+2][j-1] !=0 and '♚' and board[x-1][j-1] not in black:

    #exclude the possible alignments where ally's piece collide and add possible captures
    #return the dictionnary
    return possibleMoves


def PlayerPlay(possibleMoves: list, board: list):
    pass
    
def computerPlay(possibleMoves: list, board: list):
    pass

def isCheckmate(board: list):
    pass

def isCheck(board: list):
    pass

def isDraw(board: list):
    pass


#create the pieces and put them in a list
global pieces
pieces = []
whitePawn = Piece('Pawn', '♙', 0, 1, 'p').appendPieces(pieces)
whiteBishop = Piece('Bishop', '♗', 0, 3, 'b').appendPieces(pieces)
whiteKnight = Piece('Knight', '♘', 0, 3, 'n').appendPieces(pieces)
whiteRook = Piece('Rook', '♖', 0, 5, 'r').appendPieces(pieces)
whiteQueen = Piece('Queen', '♕', 0, 9, 'q').appendPieces(pieces)
whiteKing = Piece('King', '♔', 0, 0, 'k').appendPieces(pieces)
blackPawn = Piece('Pawn','♟', 1, 1, 'P').appendPieces(pieces)
blackBishop = Piece('Bishop','♝', 1, 3, 'B').appendPieces(pieces)
blackKnight = Piece('Knight','♞', 1, 3, 'N').appendPieces(pieces)
blackRook = Piece('Rook','♜', 1, 5, 'R').appendPieces(pieces)
blackQueen = Piece('Queen','♛', 1, 9, 'Q').appendPieces(pieces)
blackKing = Piece('King','♚', 1, 0, 'K').appendPieces(pieces)


if __name__ == "__main__":
    chessBoard = getBoard()
    setBoard(chessBoard, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", pieces)
    printBoard(chessBoard)
    x = possibleMoves(pieces, chessBoard)
    print(x)
