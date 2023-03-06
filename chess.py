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
    """Return a piece's name"""
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

                
def modifyFen(originalFen: str, pieces: list):
    newFen = originalFen
    return newFen

def Play(board: list, FEN: str):
    #fenstring tells us which turn is it to play, black or white
    for char in FEN:
        pass

def possibleMoves(pieces: list, board: list, name: str):
    return name

    
#create the pieces and put them in a list
global pieces
pieces = []
whitePawn = Piece('pawn', '♙', 0, 1, 'p').appendPieces(pieces)
whiteBishop = Piece('bishop', '♗', 0, 3, 'b').appendPieces(pieces)
whiteKnight = Piece('knight', '♘', 0, 3, 'n').appendPieces(pieces)
whiteRook = Piece('rook', '♖', 0, 5, 'r').appendPieces(pieces)
whiteQueen = Piece('queen', '♕', 0, 9, 'q').appendPieces(pieces)
whiteKing = Piece('king', '♔', 0, 0, 'k').appendPieces(pieces)
blackPawn = Piece('pawn', '♟', 1, 1, 'P').appendPieces(pieces)
blackBishop = Piece('bishop', '♝', 1, 3, 'B').appendPieces(pieces)
blackKnight = Piece('knight', '♞', 1, 3, 'N').appendPieces(pieces)
blackRook = Piece('rook', '♜', 1, 5, 'R').appendPieces(pieces)
blackQueen = Piece('queen', '♛', 1, 9, 'Q').appendPieces(pieces)
blackKing = Piece('king', '♚', 1, 0, 'K').appendPieces(pieces)


if __name__ == "__main__":
    chessBoard = getBoard()
    setBoard(chessBoard, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", pieces)
    printBoard(chessBoard)
    


