import random, sys

class Piece:
    def __init__(self, unicode: str, color: int, value: int, fenName: str):
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
    #get the corresponding fstring from the pieces: list unicodes
    possibleMoves = {}
    for piece in pieces:
        possibleMoves[piece.getUnicode()] = piece.getFen()
    
    #loop over the board to check each piece's alignments, by incrementing or decrementing their board[x+-1/8][j+-1/8] values
    for x in range(len(board)):
        for j in range(len(board[x])):
            pass
    #exclude the possible alignments where ally's piece collide and add possible captures
    #separate black and white's possible moves with 2 keys in 1 dictionnary
    #return the dictionnary
    return possibleMoves
    
def PlayerPlay(possibleMoves: list, board: list):
    pass
    
    
#create the pieces and put them in a list
global pieces
pieces = []
whitePawn = Piece('♙', 0, 1, 'p').appendPieces(pieces)
whiteBishop = Piece('♗', 0, 3, 'b').appendPieces(pieces)
whiteKnight = Piece('♘', 0, 3, 'n').appendPieces(pieces)
whiteRook = Piece('♖', 0, 5, 'r').appendPieces(pieces)
whiteQueen = Piece('♕', 0, 9, 'q').appendPieces(pieces)
whiteKing = Piece('♔', 0, 0, 'k').appendPieces(pieces)
blackPawn = Piece('♟', 1, 1, 'P').appendPieces(pieces)
blackBishop = Piece('♝', 1, 3, 'B').appendPieces(pieces)
blackKnight = Piece('♞', 1, 3, 'N').appendPieces(pieces)
blackRook = Piece('♜', 1, 5, 'R').appendPieces(pieces)
blackQueen = Piece('♛', 1, 9, 'Q').appendPieces(pieces)
blackKing = Piece('♚', 1, 0, 'K').appendPieces(pieces)


if __name__ == "__main__":
    chessBoard = getBoard()
    setBoard(chessBoard, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", pieces)
    printBoard(chessBoard)
    a = possibleMoves(pieces, chessBoard)
    print(a)
    
    


